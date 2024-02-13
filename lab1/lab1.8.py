l = []

while True:
    a = input()
    if a == '!':
        break
    l.append(int(a))

result = list(filter(lambda x: x >= 150 and x <= 190, l))

print(len(result))
print('{} {}'.format(min(result), max(result)))
