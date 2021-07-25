import jsonpickle
from file_handler import FileHandler


class Storage:
    def __init__(self, file_name):
        self.file_handler = FileHandler()
        self.path = self.file_handler.get_file_path(file_name)

    def save_data(self, file):
        json_data = jsonpickle.encode(file)
        self.file_handler.write(self.path, json_data)

    def update_data(self, item):
        data = self.get_data()
        updated_list = []
        for i in data:
            if i.id == item.id:
                updated_list.append(item)
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
        data = self.get_data()
        if len(data) == 0:
            id = 1
        else:
            item = data[-1]
            id = item.id + 1
        return id

    def get_by_id(self, id):
        data = self.get_data()
        for item in data:
            if item.id == id:
                return item
