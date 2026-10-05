--Знайти оцінки студентів у окремій групі з певного предмета.
SELECT s.id AS student_id, m.grade
FROM students s
JOIN marks m ON s.id=m.id
JOIN subjects sub ON sub.id=m.id_subject
JOIN groups g ON s.group_id=g.id
WHERE m.id_subject=2
WHERE g.id=1 