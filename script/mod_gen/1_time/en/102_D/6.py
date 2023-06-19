def solve():
    N = int(input())
    A = list(map(int, input().split()))
    S = sum(A)
    a = []
    for i in range(N-1):
        S -= 2*A[i]
        a.append(S)
    print(min(a))
solve()
