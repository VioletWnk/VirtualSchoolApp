from storage import Storage
from school import School
from validate import Validate


class SchoolStorage(Storage):
    def __init__(self, file_name='school_storage.json'):
        super().__init__(file_name)
        self.validate = Validate()

    def add(self):
        school_id = self.generate_id()
        school_name = self.validate.get_str('Введите название школы')
        school_address = self.validate.get_str('Введите адрес')

        schools = self.get_data()

        schools.append(School(school_id, school_name, school_address))
        self.save_data(schools)

    def get(self):
        self.show()
        school_id = self.validate.get_int('Введите номер школы, чтобы получить информацию')
        school = self.get_by_id(school_id)
        print(f'\nНазвание школы: {school.name}\nАдрес школы: {school.address}\n\n')

    def update(self):
        self.show()
        school_id = self.validate.get_int('Введите номер школы, чтобы изменить информацию')
        school = self.get_by_id(school_id)

        school_name = input('Введите название (нажмите enter, чтобы пропустить этот шаг): ')
        if school_name != '':
            school.name = school_name
        school_address = input('Введите новый адрес (нажмите enter, чтобы пропустить этот шаг): ')
        if school_address != '':
            school.address = school_address

        self.update_data(school)

    def show(self):
        school_data = self.get_data()
        row = '№'
        name = 'Название школы'
        print(f'|{row}|{name:20}|')
        for school in school_data:
            print(f'|{school.id}|{school.name:20}|')






