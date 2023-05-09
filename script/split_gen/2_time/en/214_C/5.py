def solve():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        j = (i - 1) % N
        ans[i] = T[i]
        while j != i:
            if ans[j] + S[j] <= ans[i]:
                ans[j] += S[j]
            else:
                ans[j] = ans[i]
            j = (j - 1) % N
    print(*ans, sep='
')
solve()
