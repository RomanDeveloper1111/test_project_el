import {useEffect, useState} from "react";
import axios from "axios";
import {useParams} from "react-router-dom";
import {Grid, Link, Typography} from "@mui/material";
import styles from './common.module.css'


const PostDetails = () => {
    const {id} = useParams()
    const [post, setPost] = useState({})

    useEffect(() => {

        if(!id) return
        const fetchData = async () => {
            const response = await axios.get(`http://localhost:8000/api/posts/${id}`)

            setPost(response.data)
        }

        fetchData()
    }, [id])

    return (
        <Grid className={styles.post_detail_grid} container>
            <Grid item xs={8}>
                <Typography variant='body2'>
                    {post.title}
                </Typography>
                <Typography variant='body2'>
                    {post.content}
                </Typography>
            </Grid>
            <Grid item xs={4}>
                <img src={`http://localhost:8000${post.image_s}`} alt=""/>
            </Grid>
        </Grid>


    )

}

export default PostDetails