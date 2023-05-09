def solve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        return
    diff = []
    for i in range(M-1):
        diff.append(X[i+1]-X[i])
    diff.sort()
    ans = sum(diff[:M-N])
    print(ans)

if __name__ == '__main__':
    solve()