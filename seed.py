from datetime import datetime
from faker import Faker
from connect import session
import random
from models import Group,Student,Subject,Journal,Teacher

groups = ['КБ-21','КБ-22','КБ-23']
subjects = ['Алгебра','Фізика','Англійська мова','Хімія','Фізкультура']

fake = Faker('uk_UA')

def fill_students():
    group_objects = session.query(Group).all()
    for _ in range(30):
        student = Student(full_name = fake.name(), group = random.choice(group_objects))
        session.add(student)

def fill_groups():
    for g in groups:
        group_ = Group(name = g)
        session.add(group_)

def fill_teachers():
    for _ in range(5):
        teacher = Teacher(full_name = fake.name())
        session.add(teacher)

def fill_subjects():
    teacher_objects = session.query(Teacher).all()
    for s in subjects:
        teacher_id = random.choice(teacher_objects).id
        subject = Subject(name = s,teacher_id = teacher_id)
        session.add(subject)

def fill_journal():
    subjects  = session.query(Subject).all()
    students = session.query(Student).all()

    for student in students:
        for subject in subjects:
            for _ in range(20):
                journal = Journal(student_id  = student.id,subject_id = subject.id,grade = random.randint(1,5), date = fake.date_between(start_date="-1y", end_date="today"))
                session.add(journal)

def main():
    fill_groups()
    fill_students()
    fill_teachers()
    fill_subjects()
    fill_journal()

    session.commit()

if __name__ == '__main__':
    main()