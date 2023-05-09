def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    visited = [False] * n
    visited[0] = True
    now = 0
    cnt = 0
    while True:
        now = a[now] - 1
        cnt += 1
        if visited[now]:
            break
        visited[now] = True
    k -= cnt
    k %= cnt
    for _ in range(k):
        now = a[now] - 1
    print(now + 1)
