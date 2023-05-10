def main():
    n = int(input())
    a = 1
    b = 2 * n + 1
    while True:
        if a == b:
            print(a)
            break
        c = (a + b) // 2
        print(c)
        d = int(input())
        if d == 0:
            break
        elif d == -1:
            b = c
        else:
            a = c + 1
