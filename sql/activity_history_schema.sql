
CREATE DATABASE yeli_activity_history;
CREATE USER yeli;
GRANT ALL PRIVILEGES ON DATABASE yeli TO yeli_activity_history;
\c yeli_activity_history

CREATE TABLE tweets (
    user_id interger,
    tweet_id integer,
    PRIMARY KEY(user_id, tweet_id)
);
CREATE UNIQUE INDEX tweets_gist_index ON tweets USING GIST (user_id, tweet_id);

CREATE TABLE twitter_likes (
    user_id interger,
    tweet_id integer,
    PRIMARY KEY(user_id, tweet_id)
);
CREATE UNIQUE INDEX twitter_likes_gist_index ON twitter_likes USING GIST (user_id, tweet_id);

CREATE TABLE instagram_posts (
    username text,
    id integer,
    PRIMARY KEY(username, id)
);
CREATE UNIQUE INDEX instagram_posts_gist_index ON instagram_posts USING GIST (username, id);
