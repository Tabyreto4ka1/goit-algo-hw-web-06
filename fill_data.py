from datetime import datetime, timedelta

import faker
import random
import sqlite3

NUMBER_STUDENTS=30
NUMBER_GROUPS=3
NUMBER_TEACHERS=5
NUMBER_SUBJECTS=6



def generate_fake_data(students, teachers, subjects) :

    fake_subjects=subjects  #Так як Faker немає функції для предметів, просто беремо список предметів , які записали 
    fake_teachers = []
    fake_students = []  
    fake_data = faker.Faker()

    for _ in range(students):
        fake_students.append(fake_data.name())


    for _ in range(teachers):
        fake_teachers.append(fake_data.name())



    return fake_students ,  fake_teachers ,  fake_subjects      



def prepare_data(students, teachers, subjects) :
    for_students = []
    for student_name in students:

        """Для таблиці студентів id автоматично створюється, а ім'я беремо фейкове, яке нам створило Faker.
        Дя номера группи беремо випадкове значення від 1 до кількості групп (3)"""

        for_students.append((student_name, random.randint(1, NUMBER_GROUPS) ))          

    for_teachers = [] 
    for teacher in teachers:

        """Для вчителів id теж автоматично створюється та ім'я ми беремол фейкове"""

        for_teachers.append((teacher, ))

    for_subjects = []

    for subject in subjects:

        """Для предметів id створюється автоматично, предмет береться зі списку, але його потрібео свторювати самому,
        бо Faker не надає такої можливості, teacher_id визначаємо випадково в діапазоні всіх вчителів"""

        for_subjects.append((subject, random.randint(1,NUMBER_TEACHERS)))

    for_marks=[]
    id_student = 0
    date_now=datetime.now()
    for id_student in range(NUMBER_STUDENTS):

        """Для оцінок student_id робимо від 1 до NUMBER_STUDENTS включно разів, для grade беремо випадкову кількість від 5 до 15
        і потім генеруємо від 1 до 12, для date_received беремо випадкове значення в діпазоні 1-365 днів від сьогодні,
        id_subject визначаємо випадково від 1 до NUMBER_SUBJECTS """

        id_student+=1
        number_of_marks= random.randint(5,15)
        for _ in range(number_of_marks):
            random_date= date_now - timedelta(days=random.randint(1,365))
            for_marks.append((id_student,random.randint(1,12),str(random_date) , random.randint(1,NUMBER_SUBJECTS) ))


    return for_students, for_teachers, for_subjects, for_marks


def insert_data_to_db(students, teachers, subjects, marks) -> None:

    """Встановлюємо з'єднання і для кожної таблиці пишемо скрипт sql_..., який потім
     вконуємо через execute або executemany. Після виконання усіх скриптів записуємо через commit"""

    with sqlite3.connect('task.db') as con:

        cur = con.cursor()

        sql_group= """INSERT INTO groups DEFAULT VALUES """
        for _ in range(NUMBER_GROUPS):
            cur.execute(sql_group)

        sql_students="""INSERT INTO students ( student_name, group_id)
        VALUES (?,?)"""
        cur.executemany(sql_students, students)

        sql_teachers=""" INSERT INTO teachers (teacher_name)
        VALUES(?)"""
        cur.executemany(sql_teachers, teachers)

        sql_subjects="""INSERT INTO subjects (subject_name, teacher_id)
        VALUES(?,?)"""
        cur.executemany(sql_subjects, subjects)

        sql_marks="""INSERT INTO marks (student_id, grade, date_received, id_subject )
        VALUES(?,?,?,?)"""
        cur.executemany(sql_marks, marks)
        
        con.commit()


if __name__ == "__main__":
    subjects_all=["Mathematics", "Physics", "Chemistry", "Biology", "History", "Geography"] #Список предметів
    students, teachers, subjects, marks= prepare_data(*generate_fake_data(NUMBER_STUDENTS,NUMBER_TEACHERS,subjects_all))
    insert_data_to_db(students, teachers, subjects, marks)