
CREATE DATABASE yeli_subs;
CREATE USER yeli;
GRANT ALL PRIVILEGES ON DATABASE yeli TO yeli_subs;
\c yeli_subs

CREATE TABLE users (
    id integer PRIMARY KEY,
    twitter_token text UNIQUE,
    first_name text,
    last_name text,
    username text,
    title text
);

CREATE TABLE twitter_targets (
    id integer PRIMARY KEY,
    name text NOT NULL,
);

CREATE TABLE instagram_targets (
    username integer PRIMARY KEY,
    name text NOT NULL,
);

CREATE TABLE twitter_sub (
    user_id integer REFERENCES users ON DELETE CASCADE ON UPDATE CASCADE,
    target_id integer REFERENCES twitter_targets ON DELETE RESTRICT ON UPDATE RESTRICT,
    PRIMARY KEY (user_id, target_id)
);

CREATE TABLE instagram_sub (
    user_id integer REFERENCES users ON DELETE CASCADE ON UPDATE CASCADE,
    target_id integer REFERENCES instagram_targets ON DELETE RESTRICT ON UPDATE RESTRICT,
    PRIMARY KEY (user_id, target_id)
);
