import {AppBar, Toolbar, IconButton, Typography} from "@mui/material";
import styles from "./navbar.module.css";


function NavBar(){
    return (
        <AppBar className={styles.item} position="static">
            <Toolbar variant="dense">
                <IconButton edge="start" color="inherit" aria-label="menu" sx={{mr: 2}}>

                </IconButton>
                <Typography variant="h6" color="inherit" component="div">
                    Small System Blog
                </Typography>
            </Toolbar>
        </AppBar>
    )
}

export default NavBar
