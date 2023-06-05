def solve():
    # print("solve")
    N = 2 ** 20
    # print(N)
    A = [-1] * N
    # print(A)
    Q = int(input())
    # print(Q)
    for i in range(Q):
        # print(i)
        t, x = map(int, input().split())
        # print(t)
        # print(x)
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        else:
            print(A[x % N])
solve()
