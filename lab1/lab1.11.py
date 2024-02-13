h = int(input())
for x in range(0, h):
    n = x * 2 + 1
    m = h - (x + 1)
    print('{}{}'.format(' ' * m, '*' * n))
