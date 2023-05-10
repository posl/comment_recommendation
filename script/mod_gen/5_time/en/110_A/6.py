def allowance():
    allowance = 0
    a, b, c = input().split()
    if a == b == c:
        allowance = int(a + b + c) * 3
    elif a == b:
        allowance = int(a + b) * 2 + int(c)
    elif a == c:
        allowance = int(a + c) * 2 + int(b)
    elif b == c:
        allowance = int(b + c) * 2 + int(a)
    else:
        allowance = int(a) + int(b) + int(c)
    print(allowance)
allowance()

if __name__ == '__main__':
    allowance()