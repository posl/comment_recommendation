def solve():
    N = input()
    k = len(N)
    N = int(N)
    if k == 1:
        if N % 3 == 0:
            print(0)
        else:
            print(-1)
        return
    a = [0] * 3
    for i in range(k):
        a[int(N % 3)] += 1
        N //= 10
    if (a[1] + 2 * a[2]) % 3 == 0:
        print(0)
        return
    if k == 2:
        print(-1)
        return
    if a[1] > 0:
        print(1)
        return
    print(2)
