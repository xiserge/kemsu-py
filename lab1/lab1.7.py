def s(a1, a2):
    if a1 > a2:
        return a2, a1
    return a1, a2


n = int(input())

a1 = n % 10
n = int(n / 10)
a2 = n % 10
n = int(n / 10)
a3 = n % 10
a4 = int(n / 10)

a1, a2 = s(a1, a2)
a1, a3 = s(a1, a3)
a1, a4 = s(a1, a4)

a2, a3 = s(a2, a3)
a2, a4 = s(a2, a4)

a3, a4 = s(a3, a4)

print('{}{}{}{}'.format(a1, a2, a3, a4))
