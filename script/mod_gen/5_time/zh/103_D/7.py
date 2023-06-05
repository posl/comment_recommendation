def solve():
    N, M = map(int, input().split())
    a = []
    b = []
    for i in range(M):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    ans = 0
    for i in range(N-1):
        if a[-1] <= i+1 and i+1 <= b[0]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()