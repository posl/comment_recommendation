def main():
    n, m, k = map(int, input().split())
    friends = [set() for _ in range(n)]
    blocks = [set() for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        friends[a].add(b)
        friends[b].add(a)
    for _ in range(k):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        blocks[c].add(d)
        blocks[d].add(c)
    ans = [0] * n
    for i in range(n):
        ans[i] = n - len(friends[i]) - 1 - len(blocks[i])
        for j in friends[i]:
            if i in friends[j]:
                ans[i] -= 1
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    main()