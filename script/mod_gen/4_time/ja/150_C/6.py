def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    def dfs(a, l):
        if len(a) == n:
            return int("".join(map(str, a)))
        for i in range(1, n+1):
            if i in a:
                continue
            a.append(i)
            l.append(dfs(a, l))
            a.pop()
        return l
    l = dfs([], [])
    print(abs(l.index(int("".join(map(str, p)))) - l.index(int("".join(map(str, q))))))

if __name__ == '__main__':
    main()