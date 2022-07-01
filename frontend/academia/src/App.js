import Header from "./components/Header";
import Footer from "./components/Footer";
import Login from "./pages/Login";
import Secretary from "./pages/Secretary";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import "./App.css";

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" exact element={<Login />} />
        <Route path="/secretary" exact element={<Secretary />} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
