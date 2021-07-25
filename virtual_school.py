from menu import Menu
from school_storage import SchoolStorage
from student_storage import StudentStorage


class VirtualSchool:
    def __init__(self):
        self.menu = Menu()
        self.school_storage = SchoolStorage()
        self.student_storage = StudentStorage()

    def start(self):
        while True:
            item = self.menu.main_menu()

            if item == Menu.ITEM_ADD_SCHOOL:
                self.school_storage.add()
            if item == Menu.ITEM_GET_SCHOOL:
                self.school_storage.get()
            if item == Menu.ITEM_UPDATE_SCHOOL:
                self.school_storage.update()
            if item == Menu.ITEM_GET_STUDENTS:
                self.student_storage.get()
            if item == Menu.ITEM_ADD_STUDENT:
                self.student_storage.add()
            if item == Menu.ITEM_REMOVE_STUDENT:
                self.student_storage.remove()
            if item == Menu.ITEM_EXIT:
                break







