n = [int(x) for x in input()]
n.sort()
if len(n) != 3:
    print('Вы ввели не трехзначное число')
elif n[0] + n[2] == n[1] * 2:
    print('Вы ввели красивое число')
else:
    print('Жаль, вы ввели обычное число')
