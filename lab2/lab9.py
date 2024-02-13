s = input()
p = 9
for i in s:
    np = int(i)
    if np > p:
        print(np, end='')
    p = np
print('')