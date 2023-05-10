def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    cd = [list(map(int, input().split())) for _ in range(m)]
    def check(p):
        for a, b in ab:
            if (p.index(a) < p.index(b)) != (a in p[:p.index(b)]):
                return False
        for c, d in cd:
            if (p.index(c) < p.index(d)) != (c in p[:p.index(d)]):
                return False
        return True
    def dfs(s, p):
        if len(p) == n:
            if check(p):
                print('Yes')
                exit()
            return
        for i in range(s, n + 1):
            dfs(i + 1, p + [i])
    dfs(1, [])
    print('No')

if __name__ == '__main__':
    main()