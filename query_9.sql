--Знайти список курсів, які відвідує студент.
SELECT s.id AS student_id,s.student_name, m.id_subject 
FROM students s 
JOIN marks m ON s.id=m.student_id
WHERE s.id = 2
GROUP BY m.id_subject