age = int(input("Возраст: "))

def person_age(age):
    if age < 3:
        exit
    elif 3 <= age < 6:
        return "Учиться в детском саду"
    elif 6 <= age < 18:
        return "Учиться в школе"
    elif 18 <= age < 23:
        return "Учиться в ВУЗе"
    else:
        return "Надо работать"

p = person_age(age)
print(p)