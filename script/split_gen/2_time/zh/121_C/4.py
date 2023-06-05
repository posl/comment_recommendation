def solve():
    N, M, C = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    count = 0
    for a in A:
        sum = C
        for i in range(M):
            sum += a[i] * B[i]
        if sum > 0:
            count += 1
    print(count)
solve()
