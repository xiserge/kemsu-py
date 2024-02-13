tall = []

while True:
    a = input()
    if a == '!':
        break
    tall.append(int(a))

result = list(filter(lambda x: 150 <= x <= 190, tall))

print(len(result))
print('{} {}'.format(min(result), max(result)))
