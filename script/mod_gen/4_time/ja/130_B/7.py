def solve():
    N, X = [int(i) for i in input().split()]
    L = [int(i) for i in input().split()]
    D = 0
    ans = 1
    for i in range(N):
        D += L[i]
        if D <= X:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()