def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    now = 1
    visited = [False] * (n + 1)
    visited[1] = True
    for i in range(k):
        now = a[now - 1]
        if visited[now]:
            break
        visited[now] = True
    if i == k - 1:
        print(now)
    else:
        loop = []
        loop.append(now)
        while True:
            now = a[now - 1]
            if now == loop[0]:
                break
            loop.append(now)
        print(loop[(k - i - 1) % len(loop)])

if __name__ == '__main__':
    main()