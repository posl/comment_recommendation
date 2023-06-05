def solve():
    n,m = map(int,input().split())
    bridges = []
    for i in range(m):
        a,b = map(int,input().split())
        bridges.append((a,b))
    bridges.reverse()
    islands = [set() for _ in range(n)]
    ans = 0
    for a,b in bridges:
        a -= 1
        b -= 1
        ans += len(islands[a]) * len(islands[b])
        islands[a] |= islands[b] | {b}
        islands[b] = islands[a]
    print(ans)

if __name__ == '__main__':
    solve()