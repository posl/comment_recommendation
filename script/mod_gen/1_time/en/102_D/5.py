def solve():
    n = int(input())
    A = list(map(int, input().split()))
    cumsum = [0]
    for a in A:
        cumsum.append(cumsum[-1] + a)
    ans = float('inf')
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            P = cumsum[i]
            Q = cumsum[j] - cumsum[i]
            R = cumsum[n] - cumsum[j]
            S = cumsum[n] - cumsum[j]
            ans = min(ans, max(P, Q, R, S) - min(P, Q, R, S))
    print(ans)

if __name__ == '__main__':
    solve()