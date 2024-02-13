login = input()
email = input()

if '@' not in login and '@' in email:
    correct = True
else:
    correct = False

if correct:
    print('ВЕРНО')
else:
    print('НЕВЕРНО')
