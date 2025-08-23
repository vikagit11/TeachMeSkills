-- 📘 TeachMeSkills: Домашнее задание по SQL
-- Тема: Создание таблиц, связи и JOIN
--
-- 📌 Примеры:
-- Создать таблицу:
-- CREATE TABLE example (
--     id INT PRIMARY KEY,
--     name VARCHAR(255)
-- );
--
-- Вставить данные:
-- INSERT INTO example (id, name) VALUES (1, 'Пример');
--
-- Пример INNER JOIN:
-- SELECT a.id, b.name FROM table_a a
-- INNER JOIN table_b b ON a.id = b.a_id;
--
-- Пример агрегатной функции:
-- SELECT author_id, SUM(quantity) FROM sales
-- JOIN books ON sales.book_id = books.id
-- GROUP BY author_id;
--
-- 💡 Вопросы для самоконтроля:
-- 1. Чем отличается INNER JOIN от LEFT JOIN?
-- 2. Почему внешний ключ важен для целостности данных?
-- 3. Для чего нужен GROUP BY?

-- 📋 Задача 1: Создание и заполнение таблиц
-- TODO: Создайте таблицу authors с полями id, first_name, last_name
--       (используйте PRIMARY KEY для поля id)
CREATE TABLE authors (
    id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
 );

-- TODO: Создайте таблицу books с полями id, title, author_id, publication_year
--       (PRIMARY KEY — id, FOREIGN KEY — author_id, ссылается на authors)
CREATE TABLE books (
    id INT PRIMARY KEY,
    title VARCHAR(255),
    author_id INT,
    publication_year INT,
    Foreign Key (author_id) REFERENCES authors(id)
 );

-- TODO: Создайте таблицу sales с полями id, book_id, quantity
--       (PRIMARY KEY — id, FOREIGN KEY — book_id, ссылается на books)
CREATE TABLE sales (
    id INT PRIMARY KEY,
    book_id INT,
    quantity INT,
    Foreign Key (book_id) REFERENCES books(id)
 );

-- TODO: Добавьте нескольких авторов в таблицу authors
--       (INSERT INTO authors ...)
INSERT INTO authors (id, first_name, last_name) VALUES (1, 'Лев', 'Толстой'),
                                                       (2, 'Антон', 'Чехов'),
                                                       (3, 'Михаил', 'Булгаков');
                                                       
-- TODO: Добавьте несколько книг в таблицу books, указывая авторов из authors
INSERT INTO books (id, title, author_id, publication_year) VALUES (1, 'Война и мир', 1, 1869),
                                                               (2, 'Чайка', 2, 1896),
                                                              (3, 'Мастер и Маргарита', 3, 1967);

-- TODO: Добавьте записи о продажах книг в таблицу sales
INSERT INTO sales (id, book_id, quantity) VALUES (1, 1, 500),
                                                       (2, 2, 400),
                                                       (3, 3, 300);

-- 📋 Задача 2: Использование JOIN
-- TODO: Используйте INNER JOIN, чтобы получить список всех книг и их авторов
-- 💡 Пример:
-- SELECT books.title, authors.first_name, authors.last_name
-- FROM books
-- INNER JOIN authors ON books.author_id = authors.id;

SELECT books.title, authors.first_name, authors.last_name, books.publication_year
FROM books
INNER JOIN authors ON books.author_id = authors.id;

-- TODO: Используйте LEFT JOIN, чтобы получить список всех авторов и их книг
--       (включая авторов без книг)
-- 💡 Пример:
-- SELECT authors.first_name, authors.last_name, books.title
-- FROM authors
-- LEFT JOIN books ON books.author_id = authors.id;
SELECT authors.first_name, authors.last_name, books.title
FROM authors
LEFT JOIN books ON books.author_id = authors.id;

-- TODO: Используйте RIGHT JOIN, чтобы получить список всех книг и их авторов
--       (включая книги без автора)
-- 💡 Пример:
-- SELECT books.title, authors.first_name, authors.last_name
-- FROM books
-- RIGHT JOIN authors ON books.author_id = authors.id;
SELECT books.title, authors.first_name, authors.last_name
FROM authors
RIGHT JOIN books ON authors.id = books.author_id;




-- 📋 Задача 3: Множественные JOIN
-- TODO: Используйте INNER JOIN, чтобы связать authors, books и sales и получить
--       список всех книг, их авторов и продаж
-- 💡 Пример:
-- SELECT authors.first_name, authors.last_name, books.title, sales.quantity
-- FROM sales
-- INNER JOIN books ON sales.book_id = books.id
-- INNER JOIN authors ON books.author_id = authors.id;

SELECT 
    books.title,
    authors.first_name,
    authors.last_name,
    sales.quantity
FROM books
INNER JOIN authors ON books.author_id = authors.id
INNER JOIN sales ON books.id = sales.book_id;

-- TODO: Используйте LEFT JOIN, чтобы связать authors, books и sales и получить
--       список всех авторов, их книг и продаж (включая авторов без книг и книги без продаж)
-- 💡 Пример:
-- SELECT authors.first_name, authors.last_name, books.title, sales.quantity
-- FROM authors
-- LEFT JOIN books ON books.author_id = authors.id
-- LEFT JOIN sales ON sales.book_id = book_id


SELECT authors.first_name, authors.last_name, books.title, sales.quantity
FROM authors
LEFT JOIN books ON books.author_id = authors.id
LEFT JOIN sales ON sales.book_id = books.id;


-- 📋 Задача 4: Агрегация данных с использованием JOIN
-- TODO: Используйте INNER JOIN и агрегатные функции, чтобы определить общее
--       количество проданных книг каждого автора
-- 💡 Пример:
-- SELECT authors.first_name, authors.last_name, SUM(sales.quantity) AS total_sales
-- FROM sales
-- INNER JOIN books ON sales.book_id = books.id
-- INNER JOIN authors ON books.author_id = authors.id
-- GROUP BY authors.id;

SELECT authors.first_name, authors.last_name, SUM(sales.quantity) AS total_sales
FROM authors
INNER JOIN books ON books.author_id = authors.id
INNER JOIN sales ON sales.book_id = books.id 
GROUP BY authors.first_name, authors.last_name;


-- TODO: Используйте LEFT JOIN и агрегатные функции, чтобы определить общее
--       количество проданных книг каждого автора, включая авторов без продаж
-- 💡 Пример:
-- SELECT authors.first_name, authors.last_name, COALESCE(SUM(sales.quantity),0) AS total_sales
-- FROM authors
-- LEFT JOIN books ON books.author_id = authors.id
-- LEFT JOIN sales ON sales.book_id = books.id
-- GROUP BY authors.id;

SELECT authors.first_name, authors.last_name, COALESCE(SUM(sales.quantity),0) AS total_sales
FROM authors
LEFT JOIN books ON books.author_id = authors.id
LEFT JOIN sales ON sales.book_id = books.id
GROUP BY authors.first_name, authors.last_name;


-- 🚀 Удачи! Не бойтесь пробовать разные JOIN и GROUP BY, чтобы лучше понять, как они работают!
