def main():
    n, m, k = map(int, input().split())
    friend = [set() for i in range(n)]
    block = [set() for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        friend[a].add(b)
        friend[b].add(a)
    for i in range(k):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        block[c].add(d)
        block[d].add(c)
    ans = [0] * n
    for i in range(n):
        ans[i] = n - len(friend[i]) - 1
        for j in friend[i]:
            if i in block[j]:
                ans[i] -= 1
        if i in block[i]:
            ans[i] += 1
    print(*ans)
