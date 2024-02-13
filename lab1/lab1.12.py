n = int(input())
f = 1
r = []
for i in range(1, n + 1):
    r.append('{}'.format(i))
    if len(r) == f:
        print(' '.join(r))
        r = []
        f = f + 1
print(' '.join(r))
