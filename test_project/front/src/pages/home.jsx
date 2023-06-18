import {Grid, Typography} from "@mui/material";
import styles from "./common.module.css";
import PostCard from "./ui/post_card";
import {useEffect, useState} from "react";
import axios from "axios";


function Home(){

    const [posts, setPosts] = useState({})

    useEffect(() => {
        const fetchData = async () => {
            const response = await axios.get('http://localhost:8000/api/posts/')
            setPosts(response.data)
        }

        fetchData()

        console.log(posts)
    }, [])

    return (
            <Grid container className={styles.grid_container}>
                <Typography className={styles.typ} variant='h3'>POSTS</Typography>
                {posts.length ? (
                        posts.map(post => (
                            <Grid key={post.id} className={styles.grid_item} item xs={12}>
                                <PostCard post={post}/>
                            </Grid>
                        ))
                    ) : (<Typography variant="body2"> Loading... </Typography>)
                }
            </Grid>
    )
}

export default Home
