drop database if exists student_db;
CREATE DATABASE student_db;
USE student_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100)
);
select * from students ; 
-- SELECT COUNT(*) FROM students;


