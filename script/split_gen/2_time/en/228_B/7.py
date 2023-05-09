def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [x-1] + a
    ans = 1
    visited = [False for _ in range(n)]
    visited[0] = True
    i = 0
    while True:
        if visited[a[i]]:
            break
        else:
            visited[a[i]] = True
            ans += 1
            i = a[i]
    print(ans)
