def f():
    N = int(input())
    A = [int(i) for i in input().split()]
    result = 0
    for a in A:
        while a % 2 == 0:
            a /= 2
            result += 1
    print(result)
f()
