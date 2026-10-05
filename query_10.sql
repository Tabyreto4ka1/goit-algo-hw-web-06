--Список курсів, які певному студенту читає певний викладач.
SELECT s.id AS student_id, t.id AS teacher_id, sub.id AS subject_id, sub.subject_name
FROM students s
JOIN marks m ON s.id=m.student_id
JOIN subjects sub ON sub.id=m.id_subject
JOIN teachers t ON t.id=sub.teacher_id
WHERE s.id=3 AND t.id=5
GROUP BY sub.id