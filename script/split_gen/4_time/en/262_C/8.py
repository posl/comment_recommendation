def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    d = {}
    for i in range(N):
        l = i + a[i]
        r = i - a[i]
        if l in d:
            d[l] += 1
        else:
            d[l] = 1
        if r in d:
            ans += d[r]
    print(ans)
