import Header from "./components/Header";
import Footer from "./components/Footer";
import Login from "./pages/Login";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import "./App.css";

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" exact element={<Login />} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
