import sys

def discounted(price, discount, max_discount=20):
        try:
            price = abs(float(price))
            discount = abs(float(discount))
            max_discount = abs(int(max_discount))
            if max_discount > 99:
                raise ValueError('Слишком большая максимальная скидка')
            if discount >= max_discount:
                return price
            else:
                return price - (price * discount / 100)
        except (ValueError, TypeError):
            sys.exit("Введите корректные параметры!")
#        except KeyboardInterrupt:
#           print("\nBye")
#           sys.exit()

while True:
    try:
        price_value = input("Цена: ")
        discount_value = input("Скидка: ")
        max_discount_value = input("Макс скидка: ")
        print(discounted(price_value ,discount_value ,max_discount_value))
    except KeyboardInterrupt:
        print("\nBye")
        exit()
