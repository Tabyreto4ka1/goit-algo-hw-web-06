--Знайти список студентів у певній групі.
SELECT s.id, s.student_name
FROM students s 
WHERE group_id = 1
