from storage import Storage
from school_storage import SchoolStorage
from student import Student


class StudentStorage(Storage):
    def __init__(self, file_name='student_storage.json'):
        super().__init__(file_name)
        self.school_storage = SchoolStorage()

    def add(self):
        school_id = self.get_school_id()
        student_name = input('Введите ФИО:')
        student_age = input('Введите возраст:')
        student_course = input('Введите класс:')
        student_id = self.generate_id()

        students = self.get_data()
        students.append(Student(student_id, student_name, student_age, student_course, school_id))
        self.save_data(students)

    def show(self, school_id):
        students_data = self.get_data()
        print(f'|№|{"ФИО":50}|{"Возраст":10}|{"Класс":10}|')
        for student in students_data:
            if student.school_id == school_id:
                print(f'|{student.id}|{student.name:50}|{student.age:10}|{student.course:10}|')

    def remove(self):
        self.get()
        student_id = int(input('\nВведите номер ученика, которого хотите удалить: '))
        self.remove_data(student_id)

    def get(self):
        school_id = self.get_school_id()
        self.show(school_id)

    def get_school_id(self):
        self.school_storage.show()
        school_id = int(input('\nВведите номер школы, чтобы просмотреть учеников: '))
        return school_id