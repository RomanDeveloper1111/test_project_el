import {Card, CardContent, Grid, Link, Typography} from "@mui/material";
import styles from './post_card.module.css';

function PostCard({post}){
    return (
        <Card  className={styles.card}>
            <Grid container>
                <Grid item xs={3}>
                    <img width='260' height='255' src={`http://localhost:8000${post.image_s}`} alt=""/>
                </Grid>
                <Grid item xs={9}>
                    <CardContent>
                        <Typography className={styles.card_item}>
                            <h1 className={styles.card_item}>{post.title}</h1>
                            <h3>{new Date(post.created_at).toDateString()}</h3>
                        </Typography>
                        <Typography variant="body2" color="text.secondary" className={styles.card_item}>
                            {post.content}
                        </Typography>
                    </CardContent>

                        <Link className={styles.card_btn} href={`/posts/${post.id}/`}>Read more</Link>

                </Grid>

            </Grid>



        </Card>
    )
}


export default PostCard