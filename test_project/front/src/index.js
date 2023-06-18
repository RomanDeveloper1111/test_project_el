import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import NavBar from "./pages/ui/navbar";
import Router from "./pages/Routers";
import {Grid} from "@mui/material";
import Menu from "./pages/ui/menu";


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
      <NavBar/>
      <Grid container>
          <Grid item xs={2}>
              <Menu />
          </Grid>

          <Grid item xs={9}>
              <Router/>
          </Grid>
      </Grid>

  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
