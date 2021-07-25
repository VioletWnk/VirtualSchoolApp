from validate import Validate


class Menu:
    ITEM_ADD_SCHOOL = 1
    ITEM_GET_SCHOOL = 2
    ITEM_UPDATE_SCHOOL = 3
    ITEM_GET_STUDENTS = 4
    ITEM_ADD_STUDENT = 5
    ITEM_REMOVE_STUDENT = 6
    ITEM_EXIT = 7

    def __init__(self):
        self.validate = Validate()

    def main_menu(self):
        self.show_menu()
        return self.validate.get_int('Выберите пункт меню')

    def show_menu(self):
        list = [
            'Добавить школу',
            'Получение полной информации о школе',
            'Изменение информации о школе',
            'Просмотр учеников школы в виде таблицы',
            'Добавление нового ученика школы',
            'Удаление имеющегося ученика школы',
            'Выйти из программы'
        ]
        for id, val in enumerate(list):
            print(f'{id + 1}. {val}')
