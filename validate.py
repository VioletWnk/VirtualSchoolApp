class Validate:
    def is_valid(self, item):
        if item.isdigit():
            return True
        else:
            return False

    def is_empty(self, item):
        if item != '':
            return True
        else:
            return False

    def get_int(self, text):
        while True:
            item = input(f'{text}: ')
            if self.is_valid(item):
                return int(item)
            else:
                print('Вы ввели неверные данные')

    def get_str(self, text):
        while True:
            item = input(f'{text}: ')
            if self.is_empty(item):
                return item
            else:
                print('Вы ввели неверные данные')
