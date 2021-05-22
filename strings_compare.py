def string_comapre(string_1, string_2):
    if type(string_1) == str and type(string_2) == str:
        if string_1 == string_2:
            return 1
        elif not string_1 == string_2 and len(string_1) > len(string_2):
            return 2
        elif not string_1 == string_2 and string_2 == 'learn':
            return 3
    else:
        return "Ето не строки"

print(string_comapre(3, 'тест'))
print(string_comapre('тест', 'тест'))
print(string_comapre('тест123', 'тест'))
print(string_comapre('тест', 'learn'))