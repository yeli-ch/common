
CREATE DATABASE yeli_activity_history;
CREATE USER yeli;
GRANT ALL PRIVILEGES ON DATABASE yeli_activity_history TO yeli;
\c yeli_activity_history

CREATE TABLE tweets (
    tweet_id integer PRIMARY KEY,
    user_id integer,
    creation_time TIMESTAMP,
    content text
);

CREATE TABLE twitter_likes (
    tweet_id integer REFERENCES tweets (tweet_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    liker_id integer,
    like_time TIMESTAMP,
    PRIMARY KEY(liker_id, tweet_id)
);

CREATE TABLE retweets (
    tweet_id integer REFERENCES tweets (tweet_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    retweeter_id integer,
    retweet_time TIMESTAMP,
    PRIMARY KEY(retweeter_id, tweet_id)
);

CREATE TABLE twitter_images (
    image_id text PRIMARY KEY,
    format text,
    data text,
    tweet_id integer REFERENCES tweets (tweet_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE instagram_posts (
    post_id integer PRIMARY KEY,
    username text,
    creation_time TIMESTAMP,
    content text
);

CREATE TABLE instagram_images (
    image_id text PRIMARY KEY,
    format text,
    data text,
    post_id integer REFERENCES instagram_posts (post_id) ON DELETE CASCADE ON UPDATE CASCADE
);
