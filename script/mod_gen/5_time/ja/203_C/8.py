def solve():
    n,k = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort()
    now = k
    for i in range(n):
        a,b = ab[i]
        if now < a:
            break
        now += b
    print(now)

if __name__ == '__main__':
    solve()