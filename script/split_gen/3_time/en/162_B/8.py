def solve():
    N = int(input())
    a = 0
    b = 0
    c = 0
    for i in range(1, N+1):
        if i % 3 == 0:
            a += i
        if i % 5 == 0:
            b += i
        if i % 15 == 0:
            c += i
    print(a+b-b)
