def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[p[i] - 1] = i + 1
    for i in range(n):
        if i >= k:
            print(ans[i])
        else:
            print(-1)
