s = input()
left = len(s) // 2 + len(s) % 2 - 1
right = left + 1 - len(s) % 2
while left >= 0:
    print(' ' * left, s[left], sep='', end='')
    if right > left:
        print(' ' * (right - left - 1), s[right], sep='', end='')
    print('')
    left -= 1
    right += 1
