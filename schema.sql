DROP TABLE IF EXISTS credentials;
DROP TABLE IF EXISTS useranswers;
DROP TABLE IF EXISTS manageranswers;
DROP TABLE IF EXISTS queries;

CREATE TABLE credentials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
);

CREATE TABLE useranswers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    q1 TEXT,
    q2 TEXT,
    q3 TEXT,
    q4 TEXT,
    q5 TEXT,
    q6 TEXT,
    q7 TEXT,
    q8 TEXT,
    q9 TEXT,
    q10 TEXT,
    q11 TEXT,
    q12 TEXT,
    q13 TEXT,
    q14 TEXT,
    q15 TEXT
);

CREATE TABLE manageranswers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    managername TEXT NOT NULL,
    username TEXT NOT NULL,
    q1 TEXT,
    q2 TEXT,
    q3 TEXT,
    q4 TEXT,
    q5 TEXT,
    q6 TEXT,
    q7 TEXT,
    q8 TEXT,
    q9 TEXT,
    q10 TEXT,
    q11 TEXT,
    q12 TEXT,
    q13 TEXT,
    q14 TEXT,
    q15 TEXT
);

CREATE TABLE queries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL
);
