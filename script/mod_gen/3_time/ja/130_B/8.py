def solve():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = 0
    for i in range(1, N + 1):
        D += L[i - 1]
        if D > X:
            print(i)
            return
    print(N + 1)

if __name__ == '__main__':
    solve()