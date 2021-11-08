CREATE TABLE foreign_names (
	 id INT NOT NULL,
	 name VARCHAR(25) NOT NULL,
	 meaning VARCHAR(1000) NOT NULL,
	 gender VARCHAR(6) NOT NULL,
	 origin VARCHAR(24) NOT NULL,
	 PeoplesCount INT NULL,
	 WhenPeoplesCount TIMESTAMP NULL,
	 Source VARCHAR(10) NOT NULL
);

CREATE TABLE russian_names (
	 ID INT NOT NULL,
	 Name VARCHAR(100) NOT NULL,
	 Sex VARCHAR(1) NULL,
	 PeoplesCount INT NULL,
	 WhenPeoplesCount TIMESTAMP NULL,
	 Source VARCHAR(10) NULL
);

CREATE TABLE russian_surnames (
	 ID INT NOT NULL,
	 Surname VARCHAR(100) NOT NULL,
	 Sex VARCHAR(1) NULL,
	 PeoplesCount INT NULL,
	 WhenPeoplesCount TIMESTAMP NULL,
	 Source VARCHAR(50) NULL
);

