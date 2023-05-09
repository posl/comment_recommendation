def main():
    n,k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    s = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            s[i+1][j+1] = s[i+1][j] + s[i][j+1] - s[i][j] + a[i][j]
    def calc(m):
        b = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                b[i+1][j+1] = b[i+1][j] + b[i][j+1] - b[i][j] + (a[i][j] >= m)
        for i in range(n-k+1):
            for j in range(n-k+1):
                if b[i+k][j+k] - b[i][j+k] - b[i+k][j] + b[i][j] >= (k*k+1)//2:
                    return True
        return False
    ok, ng = 10**9, -1
    while ok - ng > 1:
        m = (ok + ng) // 2
        if calc(m):
            ng = m
        else:
            ok = m
    print(ok)

if __name__ == '__main__':
    main()