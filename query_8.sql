--Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT t.id AS teacher_id,sub.id AS subject_id ,AVG(m.grade) AS average
FROM  subjects sub
JOIN marks m ON m.id_subject=sub.id
JOIN teachers t ON sub.teacher_id=t.id
WHERE t.id=5
GROUP BY t.id, sub.id
