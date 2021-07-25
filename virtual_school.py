from menu import Menu
from school_service import SchoolService
from student_service import StudentService


class VirtualSchool:
    def __init__(self):
        self.menu = Menu()
        self.school_service = SchoolService()
        self.student_service = StudentService()

    def start(self):
        while True:
            item = self.menu.main_menu()

            if item == Menu.ITEM_ADD_SCHOOL:
                self.school_service.add()
            if item == Menu.ITEM_GET_SCHOOL:
                self.school_service.get()
            if item == Menu.ITEM_UPDATE_SCHOOL:
                self.school_service.update()
            if item == Menu.ITEM_GET_STUDENTS:
                self.student_service.get()
            if item == Menu.ITEM_ADD_STUDENT:
                self.student_service.add()
            if item == Menu.ITEM_REMOVE_STUDENT:
                self.student_service.remove()
            if item == Menu.ITEM_EXIT:
                break







