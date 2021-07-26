from student_storage import StudentStorage
from school_storage import SchoolStorage
from validate import Validate
from school import School


class SchoolService:
    def __init__(self):
        self.student_storage = StudentStorage()
        self.school_storage = SchoolStorage()
        self.validate = Validate()

    def add(self):
        school_id = self.school_storage.generate_id()
        school_name = self.validate.get_str('Введите название школы')
        school_address = self.validate.get_str('Введите адрес')

        schools = self.school_storage.get_data()

        schools.append(School(school_id, school_name, school_address))
        self.school_storage.save_data(schools)

    def get(self):
        self.show()
        school_id = self.validate.get_int('Введите номер школы, чтобы получить информацию')
        school = self.school_storage.get_by_id(school_id)
        if school is None:
            print('Такой школы нет')
        else:
            students_num = self.count_students(school_id)
            print(f'\nНазвание школы: {school.name}\nАдрес школы: {school.address}\nКоличество учеников:{students_num}\n\n')

    def update(self):
        self.show()
        school_id = self.validate.get_int('Введите номер школы, чтобы изменить информацию')
        school = self.school_storage.get_by_id(school_id)
        if school is None:
            print('Такой школы нет')
        else:
            school_name = input('Введите название (нажмите enter, чтобы пропустить этот шаг): ')
            if school_name != '':
                school.name = school_name
            school_address = input('Введите новый адрес (нажмите enter, чтобы пропустить этот шаг): ')
            if school_address != '':
                school.address = school_address

            self.school_storage.update_data(school)

    def show(self):
        school_data = self.school_storage.get_data()
        row = '№'
        name = 'Название школы'
        print(f'|{row}|{name:20}|')
        for school in school_data:
            print(f'|{school.id}|{school.name:20}|')

    def count_students(self, school_id):
        counter = 0
        students = self.student_storage.get_data()
        for student in students:
            if student.school_id == school_id:
                counter += 1
        return counter
