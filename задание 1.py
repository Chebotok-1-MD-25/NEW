x = 'Маша'
y = 18
print("Я", x, "мне", y, "лет")

d = (x + " ") * 5
print(d)

a = input('Как вас зовут?')
i = a.count(" ")
if i==0:
    print("Привет", a, "!")
    b = int(input('Сколько вам лет?'))
    if b<0 or b>150:
        print('не может быть такого')
    else:
        if b < 18:
            print("Ты такой малыыыыыыш")
        else:
            print("Извините, но вы слишком стар для меня")

        print(a[1:-1], a[::-1], a[-3:], a[0:5])

        s = str(b)
        if b<10:
            sum = int(s[0])
            pr = int(s[0])
        elif (b>=10 and b<100):
            sum = int(s[0]) + int(s[1])
            pr = int(s[0]) * int(s[1])
        else:
            sum = int(s[0]) + int(s[1]) + int(s[2])
            pr = int(s[0]) * int(s[1]) * int(s[2])
        print('Длина имени:', len(a), 'Сумма чисел возраста:', sum, 'Произведение чисел:', pr)

        print(a.upper(), a.lower(), a.capitalize(), (a.capitalize()).swapcase())
else:
    print ('Уберите пробел')




z=int(input("Сколько будет 56/4 + 6"))
if z!=20:
    print("Не правильно!")
else:
    print("Молодец!!!")


