from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, NotFound
from .serializers import UserSerializer
from .models import User
import jwt, datetime

from environ import Env

env = Env()

class RegisterView(APIView):
  def post(self, request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=201)

class LoginView(APIView):
  def post(self, request):
    email = request.data['email']
    password = request.data['password']

    user = User.objects.filter(email=email).first()

    if user is None:
      raise NotFound(detail='User not found')

    if not user.check_password(password):
      raise AuthenticationFailed('Incorrect password')

    payload = {
      'id': user.id,
      'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=int(env('JWT_TIME_IN_MINUTES'))),
      'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, env('JWT_SECRET'), algorithm=env('JWT_ALGORITHM'))

    response = Response()

    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
      'jwt': token
    }

    return response