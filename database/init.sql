CREATE DATABASE PeopleDB;

USE PeopleDB;

CREATE TABLE PeopleTable (
	PersonID int(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	Firstname VARCHAR(30) NOT NULL,
	Lastname VARCHAR(30) NOT NULL
);