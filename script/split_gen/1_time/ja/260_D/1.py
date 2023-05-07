def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = [-1] * n
    for i in range(n):
        p[i] -= 1
    for i in range(n):
        if ans[i] != -1:
            continue
        now = i
        for j in range(k):
            if ans[now] != -1:
                break
            ans[now] = i + 1
            now = p[now]
    for i in range(n):
        print(ans[i])
