
import psycopg2 as pg


class InvalidActivityException(Exception):
    pass


class ActivityHistory:

    def __init__(self, host, port, dbname, user, password):

        self.db_conn = pg.connect(host = host,
                                  port = port,
                                  dbname = dbname,
                                  user = user,
                                  password = password)
        self.db = self.db_conn.cursor()

    # TODO Is that the destructor?
    def __del__(self):
        self.db.close()
        self.db_conn.close()

    def is_activity_new(self, activity):
        if activity['type'] == "tweet":
            return self.is_tweet_new(activity)
        elif activity['type'] == "twitter_like":
            return self.is_twitter_like_new(activity)
        elif activity['type'] == "retweet":
            return self.is_retweet_new(activity)
        elif activity['type'] == "instagram_post":
            return self.is_instagram_post_new(activity)
        else:
            raise InvalidActivityException()

    def is_tweet_new(self, tweet):
        self.db.exectue("SELECT * FROM tweets WHERE tweet_id IS %s", (tweet['tweet_id']))
        return bool(self.db.fetchone() is None)

    def is_twitter_like_new(self, like):
        self.db.exectue("SELECT * FROM twitter_likes WHERE (liker_id, tweet_id) IS (%s, %s)", (like['liker_id'], like['tweet_id']))
        return bool(self.db.fetchone() is None)

    def is_retweet_new(self, retweet):
        self.db.exectue("SELECT * FROM retweets WHERE (retweeter_id, tweet_id) IS (%s, %s)", (retweet['retweeter_id'], retweet['tweet_id']))
        return bool(self.db.fetchone() is None)

    def is_instagram_post_new(self, post):
        self.db.exectue("SELECT * FROM instagram_posts WHERE post_id IS %s", (post['post_id']))
        return bool(self.db.fetchone() is None)

    def insert_activity(self, activity):
        if activity['type'] == "tweet":
            self.insert_tweet(activity)
        elif activity['type'] == "twitter_like":
            self.insert_twitter_like(activity)
        elif activity['type'] == "retweet":
            self.insert_retweet(activity)
        elif activity['type'] == "instagram_post":
            self.insert_instagram_post(activity)
        else:
            raise InvalidActivityException()

    def insert_tweet(self, tweet):
        self.db.exectue("INSERT INTO tweets (tweet_id, user_id, creation_time, content) VALUES (%s, %s, %s, %s)",
                        (tweet['tweet_id'], tweet['user_id'], tweet['creation_time'], tweet['content']))
        for image in tweet['images']:
            self.db.exectue("INSERT INTO twitter_images (image_id, format, data, tweet_id) VALUES (%s, %s, %s, %s)",
                            (image['id'], image['format'], image['data'], tweet['tweet_id']))

    def insert_twitter_like(self, like):
        self.insert_tweet(like['tweet'])
        self.db.exectue("INSERT INTO twitter_likes (tweet_id, liker_id, like_time) VALUES (%s, %s, %s)",
                        (like['tweet']['tweet_id'], like['liker_id'], like['like_time']))

    def insert_retweet(self, retweet):
        self.insert_tweet(retweet['tweet'])
        self.db.exectue("INSERT INTO retweets (tweet_id, retweeter_id, retweet_time) VALUES (%s, %s, %s)",
                        (retweet['tweet']['tweet_id'], retweet['retweeter_id'], retweet['retweet_time']))

    def insert_instagram_post(self, post):
        self.db.exectue("INSERT INTO instagram_posts (post_id, username, creation_time, content) VALUES (%s, %s, %s, %s)",
                        (post['post_id'], post['username'], post['creation_time'], post['content']))
        for image in post['images']:
            self.db.exectue("INSERT INTO twitter_images (image_id, format, data, post_id) VALUES (%s, %s, %s, %s)",
                            (image['id'], image['format'], image['data'], post['post_id']))
