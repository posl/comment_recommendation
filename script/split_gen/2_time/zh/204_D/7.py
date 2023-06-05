def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            cnt = 0
            for k in range(m):
                if a[k][0] == i and a[k][1] == j:
                    cnt += 1
            ans += cnt * cnt
    print(ans)
