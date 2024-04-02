from connect import session
from models import Student, Journal, Subject,Teacher,Group
from sqlalchemy import func,select


def select_1():
    result = session.execute(select(
        Student.id,
        Student.full_name,
        func.avg(Journal.grade).label('avg_grade')
        ).join(Journal, Student.id == Journal.student_id)
        .group_by(Student.id, Student.full_name)
        .order_by(func.avg(Journal.grade).desc())
        .limit(5)
        )
    
    return result.all()

def select_2():
    result = session.execute(select(
        Student.id,
        Student.full_name,
        func.avg(Journal.grade).label('avg_grade')
        ).join(Journal, Student.id == Journal.student_id)
        .filter(Journal.subject_id == 1)
        .group_by(Student.id, Student.full_name)
        .order_by(func.avg(Journal.grade).desc())
        .limit(1)
        )

    return result.all()

def select_3():
    result = session.execute(select(
        Group.name, 
        Subject.name, 
        func.round(func.avg(Journal.grade), 2).label('avg_grade')) 
        .join(Student, Group.id == Student.group_id) 
        .join(Journal, Student.id == Journal.student_id) 
        .join(Subject, Journal.subject_id == Subject.id) 
        .group_by(Group.id, Subject.id) 
        )

    return result.all()

def select_4():
    result = session.execute(select(
        func.round(func.avg(Journal.grade))
        .label('avg_grade')))
    
    return result.all()

def select_5():
    result = session.execute(select(
        Teacher.full_name, 
        Subject.name.label('subject'))
        .join(Subject)
        .order_by(Teacher.id)
    )

    return result.all()

def select_6():
    result = session.execute(select(
        Group.name, 
        Student.id, 
        Student.full_name)
        .join(Student, Group.id == Student.group_id)
        .filter(Group.id == 1)
        .order_by(Student.id)
        )

    return result.all()

def select_7():
    result = session.execute(select(
        Student.full_name, 
        Journal.grade)
        .join(Group, Student.group_id == Group.id)\
        .join(Journal, Journal.student_id == Student.id)\
        .join(Subject, Journal.subject_id == Subject.id)\
        .filter(Group.id == 1, Subject.id == 1)
        )
    
    return result.all()

def select_8():
    result = session.execute(select(
        Teacher.full_name, 
        Subject.name, 
        func.avg(Journal.grade).label('avg_grade')) 
        .join(Subject, Journal.subject_id == Subject.id) 
        .join(Teacher, Subject.teacher_id == Teacher.id) 
        .group_by(Subject.id, Teacher.full_name) 
        )

    return result.all()

def select_9():
    result = session.execute(select(
        Journal.student_id,
        Student.full_name, 
        Subject.name)
        .join(Journal, Journal.student_id == Student.id)\
        .join(Subject, Subject.id == Journal.subject_id)\
        .group_by(Student.full_name, Subject.name,Journal.student_id)
        )

    return result.all()

def select_10():
    result = session.execute(select(
        Teacher.full_name, 
        Subject.name, 
        Student.full_name)
        .join(Subject, Teacher.id == Subject.teacher_id)
        .join(Journal, Subject.id == Journal.subject_id)
        .join(Student, Student.id == Journal.student_id)
        .filter(Student.id == 1, Teacher.id == 4)
        .group_by(Teacher.id,Subject.id,Student.id)
         )
    
    return result.all()

def main():
    number = int(input('Введіть число для запиту до БД: '))

    
    while True:
        try:
            number = int(input('Введіть число для запиту до БД: '))
        except ValueError:
            print("Будь ласка, введіть ціле число.")
            continue

        match number:
            case 1:
                res = select_1()
                for r in res:
                    print(r)
            case 2:
                res = select_2()
                for r in res:
                    print(r)
            case 3:
                res = select_3()
                for r in res:
                    print(r)
            case 4:
                res = select_4()
                for r in res:
                    print(r)
            case 5:
                res = select_5()
                for r in res:
                    print(r)
            case 6:
                res = select_6()
                for r in res:
                    print(r)
            case 7:
                res = select_7()
                for r in res:
                    print(r)
            case 8:
                res = select_8()
                for r in res:
                    print(r)
            case 9:
                res = select_9()
                for r in res:
                    print(r)
            case 10:
                res = select_10()
                for r in res:
                    print(r)
            case _:
                print("Невірне число для запиту до БД.")


if __name__ == '__main__':
    main()