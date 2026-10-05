--Знайти 5 студентів із найбільшим середнім балом з усіх предметів
SELECT s.student_name, AVG(m.grade) AS average
FROM students s
JOIN marks m ON s.id=m.student_id
GROUP BY s.id
ORDER BY average DESC
LIMIT 5;