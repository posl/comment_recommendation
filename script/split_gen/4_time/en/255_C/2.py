def main():
    x, a, d, n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
        return
    if x < a:
        if d < 0:
            print(1)
            return
        else:
            print((a-x)//d + (1 if (a-x)%d != 0 else 0))
            return
    if x > a:
        if d > 0:
            print(1)
            return
        else:
            print((x-a)//(-d) + (1 if (x-a)%(-d) != 0 else 0))
            return
    print(n)
