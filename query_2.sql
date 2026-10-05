--Знайти студента із найвищим середнім балом з певного предмета.
SELECT s.student_name,
       sub.subject_name,
       AVG(m.grade) AS average
FROM students s
JOIN marks m ON s.id = m.student_id
JOIN subjects sub ON m.id_subject = sub.id
WHERE sub.id = 2
GROUP BY s.id, s.student_name, sub.id, sub.subject_name
ORDER BY average DESC
LIMIT 1;