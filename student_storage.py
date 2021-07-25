from storage import Storage


class StudentStorage(Storage):
    def __init__(self, file_name='student_storage.json'):
        super().__init__(file_name)



