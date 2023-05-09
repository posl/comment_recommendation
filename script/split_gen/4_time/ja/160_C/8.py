def solve():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(K + A[0])
    print(K - max([A[i + 1] - A[i] for i in range(N)]))
solve()
