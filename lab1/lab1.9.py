while True:
    p1 = input()
    p2 = input()

    if len(p1) < 8:
        print('Короткий!')
    elif '123' in p1:
        print('Простой!')
    elif p1 != p2:
        print('Различаются!')
    else:
        print('OK')
        break
