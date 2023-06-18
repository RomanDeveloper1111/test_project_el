import {List, ListItem, ListItemText, Divider, Link} from "@mui/material";
import styles from './navbar.module.css'

const Menu = () => {
    return (
        <List className={styles.menu} component="nav" aria-label="mailbox folders">
            <ListItem button>
                <Link className={styles.menu_link} href='/'>
                    <ListItemText primary="All Posts"/>
                </Link>
            </ListItem>
            <Divider/>

            <Divider light/>
            <ListItem button>
                <Link className={styles.menu_link} href='/'>
                    <ListItemText primary="About Us"/>
                </Link>
            </ListItem>
        </List>
    )
}

export default Menu