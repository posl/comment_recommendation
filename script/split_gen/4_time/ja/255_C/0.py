def main():
    x, a, d, n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
    else:
        if (x-a) % d == 0:
            a1 = int((x-a) / d) + 1
            if a1 >= 1 and a1 <= n:
                print(0)
            else:
                print(1)
        else:
            a1 = int((x-a) / d) + 1
            if a1 >= 1 and a1 <= n:
                print(0)
            else:
                if a1 < 1:
                    a1 = 1
                if a1 > n:
                    a1 = n
                a2 = a + (a1-1) * d
                if abs(a2 - x) < abs(a2+d - x):
                    print(abs(a2 - x))
                else:
                    print(abs(a2+d - x))
