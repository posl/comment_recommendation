def main():
    l, r = map(int, input().split())
    if r - l >= 2019:
        print(0)
        return
    mod = 2019
    ans = 2019
    for i in range(l, r + 1):
        for j in range(i + 1, r + 1):
            ans = min(ans, (i * j) % mod)
    print(ans)
main()
