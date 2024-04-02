from sqlalchemy import create_engine,Column, Integer, String, Date,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from connect import engine

Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer,primary_key = True)
    name = Column(String(50),nullable=False)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer,primary_key = True)
    full_name = Column(String(100),nullable=False)
    group_id = Column(Integer,ForeignKey('groups.id'),nullable=False)
    group = relationship(Group)

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer,primary_key=True)
    full_name = Column(String(100),nullable=False)

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer,primary_key=True)
    name = Column(String(50),nullable=False)
    teacher_id = Column(Integer,ForeignKey('teachers.id'),nullable=False)
    teacher = relationship(Teacher)

class Journal(Base):
    __tablename__ = 'journal'
    id = Column(Integer,primary_key=True)
    student_id = Column(Integer,ForeignKey('students.id'),nullable=False)
    subject_id = Column(Integer,ForeignKey('subjects.id'),nullable=False)
    grade = Column(Integer,nullable=False)
    date = Column(Date,nullable=False)
    student = relationship(Student)
    subject = relationship(Subject)



