n = int(input())
m = int(input())
symb = input()

print(symb * m)
for x in range(0, n - 2):
    print('{}{}{}'.format(symb, ' ' * (m - 2), symb))
print(symb * m)
