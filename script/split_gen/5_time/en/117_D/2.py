def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(40, -1, -1):
        if (k >> i) & 1:
            x = 0
            for j in range(n):
                if (a[j] >> i) & 1:
                    x += 1 << i
                else:
                    x += a[j] & ((1 << i) - 1)
            ans = max(ans, x)
        else:
            x = 0
            for j in range(n):
                if (a[j] >> i) & 1:
                    x += a[j] & ((1 << i) - 1)
                else:
                    x += 1 << i
            ans = max(ans, x)
    print(ans)
