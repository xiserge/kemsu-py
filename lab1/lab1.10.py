while True:
    try:
        n1 = int(input())
        op = input()

        if op == '+':
            n2 = int(input())
            print(n1 + n2)
        elif op == '-':
            n2 = int(input())
            print(n1 - n2)
        elif op == '*':
            n2 = int(input())
            print(n1 * n2)
        elif op == '/':
            n2 = int(input())
            print(int(n1 / n2))
        elif op == '%':
            n2 = int(input())
            print(n1 % n2)
        elif op == '!':
            if n1 == 0:
                print(0)
            elif n1 > 0:
                fact = 1
                for i in range(1, n1 + 1):
                    fact = fact * i
                print(fact)
        elif op == 'x':
            print(n1)
            break
    except:
        None
