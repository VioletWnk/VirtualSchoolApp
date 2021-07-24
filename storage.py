import jsonpickle
from file_handler import FileHandler


class Storage:
    def __init__(self, file_name):
        self.file_handler = FileHandler()
        self.path = self.file_handler.get_file_path(file_name)

    def save_data(self, schools):
        json_data = jsonpickle.encode(schools)
        self.file_handler.write(self.path, json_data)

    def update_data(self, school):
        schools = self.get_data()
        updated_list = []
        for i in schools:
            if i.id == school.id:
                updated_list.append(school)
            else:
                updated_list.append(i)
        self.save_data(updated_list)

    def remove_data(self, item_id):
        items = self.get_data()
        updated_list = []
        for i in items:
            if i.id != item_id:
                updated_list.append(i)

        self.save_data(updated_list)

    def get_data(self):
        if self.file_handler.path_is_valid(self.path):
            data_json = self.file_handler.read(self.path)
            items = jsonpickle.decode(data_json)
        else:
            items = []

        return items

    def generate_id(self):
        schools = self.get_data()
        if len(schools) == 0:
            id = 1
        else:
            school = schools[-1]
            id = school.id + 1
        return id

    def get_by_id(self, id):
        schools = self.get_data()
        for school in schools:
            if school.id == id:
                return school
