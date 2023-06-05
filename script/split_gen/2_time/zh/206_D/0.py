def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    ans = 0
    for k in d:
        ans += d[k] * (d[k] - 1) // 2
    print(n * (n - 1) // 2 - ans)
