from student_storage import StudentStorage
from school_storage import SchoolStorage
from school_service import SchoolService
from student import Student
from validate import Validate


class StudentService:
    def __init__(self):
        self.student_storage = StudentStorage()
        self.school_storage = SchoolStorage()
        self.school_service = SchoolService()
        self.validate = Validate()

    def add(self):
        school_id = self.get_school_id()
        student_name = self.validate.get_str('Введите ФИО')
        student_age = self.validate.get_int('Введите возраст')
        student_course = self.validate.get_int('Введите класс')
        student_id = self.student_storage.generate_id()

        students = self.student_storage.get_data()
        students.append(Student(student_id, student_name, student_age, student_course, school_id))
        self.student_storage.save_data(students)

    def show(self, school_id):
        students_data = self.student_storage.get_data()
        print(f'|№|{"ФИО":50}|{"Возраст":10}|{"Класс":10}|')
        for student in students_data:
            if student.school_id == school_id:
                print(f'|{student.id}|{student.name:50}|{student.age:10}|{student.course:10}|')

    def remove(self):
        self.get()
        student_id = self.validate.get_int('\nВведите номер ученика, которого хотите удалить')
        self.student_storage.remove_data(student_id)

    def get(self):
        school_id = self.get_school_id()
        self.show(school_id)

    def get_school_id(self):
        self.school_service.show()
        school_id = self.validate.get_int('\nВведите номер школы, чтобы просмотреть учеников')
        return school_id