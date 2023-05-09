def main():
    a, n = map(int, input().split())
    if n == 1:
        print(-1)
        return
    if a == 2:
        print(n)
        return
    if a == n:
        print(n + 1)
        return
    if a > n:
        print(2)
        return
    visited = [False] * 10 ** 6
    visited[1] = True
    q = [(1, 1)]
    while q:
        x, cnt = q.pop(0)
        if x == n:
            print(cnt)
            return
        nx = (x * a) % 10 ** 6
        if not visited[nx]:
            visited[nx] = True
            q.append((nx, cnt + 1))
        if x % 10 != 0:
            nx = (x % 10) * 10 ** (len(str(x)) - 1) + x // 10
            if not visited[nx]:
                visited[nx] = True
                q.append((nx, cnt + 1))
    print(-1)
