def main():
    a, b = map(int, input().split())
    if a == b:
        print(a)
        return
    if a % 2 == 0 and b % 2 == 0:
        if ((b - a) // 2) % 2 == 0:
            print(b)
        else:
            print(b + 1)
    elif a % 2 == 0 and b % 2 == 1:
        if ((b - a + 1) // 2) % 2 == 0:
            print(b ^ 1)
        else:
            print(b ^ 0)
    elif a % 2 == 1 and b % 2 == 0:
        if ((b - a - 1) // 2) % 2 == 0:
            print(a ^ (b + 1))
        else:
            print(a ^ b)
    else:
        if ((b - a) // 2) % 2 == 0:
            print(a)
        else:
            print(a ^ 1)
