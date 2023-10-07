try:
    number=int(input("Введіть число:"))
except:
    print("Помилка при введенні данних")
    exit()

a = ['1. двійкова', '2. вісімкова', '3. шіснадцятквова']
print("Виберіть систему числення, в яку необхідно перевести число:")
for x in a:
    print(x)
try:
    b = int(input("Введіть номер: "))
except:
    print("Помилка при введенні данних")
    exit()

if b == 1:
    print('Число',number,'у двійковій системі числення:')
    print(bin(number))
elif b == 2:
    print('Число', number, 'у вісімковій системі числення:')
    print(oct(number))
elif b == 3:
    print('Число', number, 'у шіснадцятковій системі числення:')
    print(hex(number))
else:
    print("Помилка при введенні данних")