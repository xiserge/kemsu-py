s = input()
ls = len(s)
half = ls // 2 + ls % 2
s2 = s[half:]+s[:half]
print(s2)


