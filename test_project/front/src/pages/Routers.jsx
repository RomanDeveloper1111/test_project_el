import {BrowserRouter, Routes, Route} from "react-router-dom";
import Home from "./home";
import PostDetails from "./PostDetails";

const Router = () => {
    return(
        <BrowserRouter>
            <Routes>
                <Route element={<Home />} path="/"/>
                <Route element={<PostDetails />} path="/posts/:id"/>
            </Routes>
        </BrowserRouter>
    )
}

export default Router