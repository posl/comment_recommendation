def main():
    n, k = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    ans = 10 ** 10
    for i in range(n - k + 1):
        for j in range(n - k + 1):
            b = []
            for m in range(k):
                for l in range(k):
                    b.append(a[i + m][j + l])
            b.sort()
            ans = min(ans, b[(k * k) // 2])
    print(ans)
