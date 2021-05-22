import sys

activities = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", \
    "Нравится курс Пайтона?": "Отличний курс", "Будеш отдыхать?": "Да"}

def ask_user():
    while True:
        try:
            question = input('Пользователь: ')
            check_var = question in activities.keys()
            if check_var:
                print('Программа: {}'.format(activities[question]))
            else:
                print("Я не понимаю")
        except KeyboardInterrupt:
            print('\nBye')
            sys.exit()

ask_user()