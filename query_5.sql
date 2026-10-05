--Знайти які курси читає певний викладач
SELECT t.teacher_name, sub.subject_name
FROM teachers t 
JOIN subjects sub ON t.id=sub.teacher_id
WHERE sub.teacher_id=5;