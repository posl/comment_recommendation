def main():
    n, x = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(1, 1 << n):
        tmp = 1
        for j in range(n):
            if i >> j & 1:
                for k in range(a[j][0]):
                    tmp *= a[j][k + 1]
        if tmp == x:
            ans += 1
    print(ans)
