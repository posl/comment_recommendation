def solve():
    n = int(input())
    apx = [list(map(int, input().split())) for _ in range(n)]
    apx.sort()
    for a, p, x in apx:
        if x > 0:
            print(p)
            break
    else:
        print(-1)
solve()
