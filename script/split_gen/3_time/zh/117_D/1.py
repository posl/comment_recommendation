def solve():
    # N, K = map(int, input().split())
    # A = list(map(int, input().split()))
    N, K = 3, 7
    A = [1, 6, 3]
    # N, K = 4, 9
    # A = [7, 4, 0, 3]
    # N, K = 1, 0
    # A = [1000000000000]
    # print(N, K)
    # print(A)
    # print("N, K = %d, %d" % (N, K))
    # print("A = %s" % (A))
    A.sort()
    # print("A = %s" % (A))
    ans = 0
    for i in range(40, -1, -1):
        count = 0
        for a in A:
            if a & (1 << i):
                count += 1
        # print("i = %d, count = %d" % (i, count))
        if count >= N - count:
            ans += (1 << i) * count
        else:
            ans += (1 << i) * (N - count)
    print(ans)
solve()
