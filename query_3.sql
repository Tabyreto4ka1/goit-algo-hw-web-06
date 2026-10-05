--Знайти середній бал у групах з певного предмета
SELECT g.id, 
    AVG(m.grade) AS average, 
    sub.subject_name
FROM students s 
JOIN groups g ON s.group_id=g.id
JOIN marks m ON s.id=m.student_id
JOIN subjects sub ON  m.id_subject=sub.id
WHERE sub.id=2
GROUP BY g.id
ORDER BY average DESC
LIMIT 3;