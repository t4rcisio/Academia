from environ import Env
from rest_framework.exceptions import AuthenticationFailed
from jwt import ExpiredSignatureError, decode

env = Env()

def check_jwt(token):
  if not token:
    raise AuthenticationFailed('Missing Token')
  
  try:
    return decode(token, env('JWT_SECRET'), algorithms=[env('JWT_ALGORITHM')])
  except ExpiredSignatureError:
    raise AuthenticationFailed('Expired Token')
