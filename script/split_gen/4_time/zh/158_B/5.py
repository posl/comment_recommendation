def problem158_b():
    n, a, b = map(int, input().split())
    if a+b == 0:
        print(0)
        return
    if a == 0:
        print(0)
        return
    if n <= a+b:
        print(n)
        return
    else:
        print(a+(n-a-b)*b)
