CREATE database Phitron;

USE Phitron;

CREATE TABLE Student(
	Roll CHAR(5) PRIMARY KEY,
    Name1 VARCHAR(50),
    Marks DOUBLE
);

DROP TABLE Student;

INSERT INTO Student
(Roll, Name1, Marks) VALUES (1, 'Jarif', 90);

SET SQL_SAFE_UPDATES = 0;
UPDATE Student
SET Name1 = 'Md. Jarif Ahmed'
WHERE Roll = 1;
SET SQL_SAFE_UPDATES = 1;