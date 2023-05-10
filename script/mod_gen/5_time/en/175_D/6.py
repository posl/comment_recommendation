def main():
    n, k = map(int, input().split())
    p = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    ans = -10**18
    for i in range(n):
        now = i
        path = []
        total = 0
        while True:
            now = p[now] - 1
            path.append(c[now])
            total += c[now]
            if now == i:
                break
        if total > 0:
            if k < len(path):
                ans = max(ans, max(path[:k]))
            else:
                ans = max(ans, total * (k // len(path) - 1) + max(path))
        else:
            ans = max(ans, max(path))
    print(ans)

if __name__ == '__main__':
    main()