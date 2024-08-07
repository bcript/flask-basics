-- table for students
CREATE TABLE IF NOT EXISTS Student (
stu_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
cg TEXT,
email TEXT
);

-- Insert mutliple entries
INSERT INTO Student (name, cg, email)
VALUES
('St Xavier', '25/13', 'xavier@holyguy.com'),
('St Franstin', '25/13', 'franstin@holyguy.com'),
('St Jovan', '25/13', 'jovan@holyguy.com');

-- display table
SELECT * FROM Student;

-- count number of entries
SELECT COUNT(*) AS stu_count
FROM Student;

-- Table for teachers with composite PK
CREATE TABLE IF NOT EXISTS Teacher (
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	dept TEXT,
	email TEXT,
	-- composite PRIMARY KEY
	PRIMARY KEY (first_name, last_name)
);

-- Dropped Teacher table
DROP TABLE Teacher;

-- Table with PK
CREATE TABLE Teacher (
	teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
	given_name TEXT NOT NULL,
	surname TEXT NOT NULL,
	gender TEXT NOT NULL,
	dept TEXT NOT NULL,
	email TEXT
);

-- Insert data into teacher table
INSERT INTO Teacher(given_name, surname, gender, dept, email)
VALUES
('Li Rong', 'Tan', 'Female', 'Mathematics', 'tanlirong@asrjc.com'),
('Shan Lin', 'Sim', 'Female', 'General Paper', 'simshanlin@asrjc.com'),
('Meng Hwee', 'Lam', 'Male', 'Computing', 'lammenghwee@asrjc.com'),
('Whiston Koh', 'Law', 'Male', 'Economics', 'lawwhistonkoh@asrjc.com');

-- Update data
UPDATE Teacher
set 
dept = 'Math'

WHERE dept='Mathematics';

-- Delete data
DELETE FROM Teacher
WHERE gender='Male';

SELECT * FROM Teacher;
