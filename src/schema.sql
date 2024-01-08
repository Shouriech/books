DROP TABLE IF EXISTS `user`;
DROP TABLE IF EXISTS `books`;
DROP TABLE IF EXISTS `reveiws`;

CREATE TABLE 'user' (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT unique NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE 'books' (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT NOT NULL,
    description TEXT NOT NULL,
    image TEXT NOT NULL,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE 'reviews' (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    review TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (id),
    FOREIGN KEY (book_id) REFERENCES books (id)
);

