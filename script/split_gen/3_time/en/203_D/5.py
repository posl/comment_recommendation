def main():
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    a.sort()
    a.sort(key=lambda x: x[1])
    a.sort(key=lambda x: x[0])
    ans = 10 ** 9
    for i in range(n - k + 1):
        for j in range(n - k + 1):
            b = []
            for l in range(k):
                b += a[i + l][j:j + k]
            b.sort()
            ans = min(ans, b[k * k // 2])
    print(ans)
