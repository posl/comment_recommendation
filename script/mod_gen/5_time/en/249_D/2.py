def solve():
    N = int(input())
    A = list(map(int, input().split()))
    d = {}
    for a in A:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            k = A[i] * A[j]
            if k in d:
                ans += d[k]
    print(ans // 2)

if __name__ == '__main__':
    solve()