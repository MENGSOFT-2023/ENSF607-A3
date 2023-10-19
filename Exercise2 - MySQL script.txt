DROP DATABASE IF EXISTS ServiceTicket;
CREATE DATABASE ServiceTicket;
USE ServiceTicket;

DROP TABLE IF EXISTS EventActivity;
CREATE TABLE EventActivity (
	ID INTEGER AUTO_INCREMENT PRIMARY KEY,
	ActivityName VARCHAR(20) NOT NULL
);

INSERT INTO EventActivity (ActivityName) 
VALUES ('Design'), ('Construction'), ('Test'), ('Password Reset');


DROP TABLE IF EXISTS EventOrigin;
CREATE TABLE EventOrigin (
	ID INT AUTO_INCREMENT PRIMARY KEY,
	OriginName VARCHAR(20) NOT NULL
);

INSERT INTO EventOrigin (OriginName)
VALUES ('Joe S.'), ('Bill B.'), ('George E.'), ('Achmed M.'), ('Rona E.');


DROP TABLE IF EXISTS EventStatus;
CREATE TABLE EventStatus (
	ID INT AUTO_INCREMENT PRIMARY KEY,
	Status VARCHAR(20) NOT NULL
);

INSERT INTO EventStatus (Status) 
VALUES ('Open'), ('On Hold'), ('In Process'), ('Deployed'), ('Deployed Failed');


DROP TABLE IF EXISTS EventClass;
CREATE TABLE EventClass (
	ID INT AUTO_INCREMENT PRIMARY KEY,
	Class VARCHAR(20) NOT NULL
);

INSERT INTO EventClass (Class) 
VALUES ('Change'), ('Incident'), ('Problem'), ('Service Request');


DROP TABLE IF EXISTS EventLog;
CREATE TABLE EventLog (
	ID INT AUTO_INCREMENT PRIMARY KEY,
	Caseid VARCHAR(20) UNIQUE NOT NULL,
	Activity VARCHAR(20) NOT NULL,
	Urgency VARCHAR(1) NOT NULL,
	Impact VARCHAR(1) NOT NULL,
 	Priority VARCHAR(1) NOT NULL,
	StartDate DATE NOT NULL,
	EndDate DATE NOT NULL,
	TicketStatus VARCHAR(20) NOT NULL,
	UpdateDateTime DATETIME NOT NULL,
	Duration INTEGER NOT NULL,
	Origin VARCHAR(20) NOT NULL,
	Class VARCHAR(20) NOT NULL,
	CONSTRAINT check_caseid_format CHECK (Caseid REGEXP '^CS_[0-9]+$')
);





