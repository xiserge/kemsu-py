s = input()
p1 = s.find('f')
p2 = s.rfind('f')
if p1 >= 0:
    print(p1)
    if p1 != p2:
        print(p2)
