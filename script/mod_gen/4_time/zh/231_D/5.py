def solve():
    N, M = map(int, input().split())
    a = [0] * N
    for i in range(M):
        A, B = map(int, input().split())
        a[A - 1] += 1
        a[B - 1] += 1
    for i in range(N):
        if a[i] % 2 == 1:
            print("No")
            return
    print("Yes")
solve()
