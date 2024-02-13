path = input()
s = path[0]
p = 0
h = 0
d = 1

for i in list(path[1:] + ' '):
    if i == '<':
        d = -1
        h += 1
    elif i == '>':
        d = 1
        h += 1

    if i == 'V' or i == ' ':
        if h > 0:
            newp = p + h * d - d
            print(' ' * (p if p < newp else newp), end='')
            print(s * h)
            h = 0
            p = newp
        else:
            print(' ' * p, end='')
            print(s)

