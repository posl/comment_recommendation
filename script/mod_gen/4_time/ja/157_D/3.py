def main():
    n, m, k = map(int, input().split())
    friend = [set() for _ in range(n)]
    block = [set() for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        friend[a-1].add(b-1)
        friend[b-1].add(a-1)
    for _ in range(k):
        c, d = map(int, input().split())
        block[c-1].add(d-1)
        block[d-1].add(c-1)
    ans = [0] * n
    for i in range(n):
        ans[i] = len(friend[i] - block[i] - {i})
    print(*ans)
main()
