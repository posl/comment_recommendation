def main():
    n, m, k = map(int, input().split())
    friends = [set() for _ in range(n)]
    block = [set() for _ in range(n)]
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
        block[c].add(d)
        block[d].add(c)
    ans = [0]*n
    for i in range(n):
        ans[i] = len(friends[i]) + len(block[i])
    for i in range(n):
        for j in friends[i]:
            if i in friends[j]:
                ans[i] -= 1
                ans[j] -= 1
    for i in range(n):
        ans[i] -= len(friends[i])
        ans[i] -= len(block[i])
        ans[i] += 1
    print(*ans)

if __name__ == '__main__':
    main()