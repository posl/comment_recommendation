def solution1():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    print(a)
    if k >= n:
        for i in range(n):
            print(k//n)
    else:
        for i in range(n):
            if a[i] == a[0]:
                print(k//n + 1)
            else:
                print(k//n)
