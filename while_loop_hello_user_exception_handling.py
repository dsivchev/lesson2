def hello_user(enter_text = ''):
    try:
        while enter_text != 'Хорошо':
            print("Как дела? ")
            enter_text = input()
    except KeyboardInterrupt:
        print("\nПока!")

hello_user()