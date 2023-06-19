def main():
    n, m, k = map(int, input().split())
    friends = [[] for _ in range(n)]
    blocks = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        friends[a-1].append(b-1)
        friends[b-1].append(a-1)
    for _ in range(k):
        c, d = map(int, input().split())
        blocks[c-1].append(d-1)
        blocks[d-1].append(c-1)
    for i in range(n):
        ans = 0
        for j in range(n):
            if i == j:
                continue
            if j in friends[i]:
                continue
            if j in blocks[i]:
                continue
            if reachable(friends, i, j, n):
                ans += 1
        print(ans, end=" ")
    print()

if __name__ == '__main__':
    main()