s = input()
p1 = s.find('h') + 1
p2 = s.rfind('h') - 1
result = s[:p1] + s[p2:p2 - p1 - 2:-1] + s[p2 + 1:]
print(result)
