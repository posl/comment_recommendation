def main():
    n = int(input())
    txa = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        t, x, a = txa[i]
        ans += a
        if i < n-1:
            t2, x2, a2 = txa[i+1]
            ans -= max(0, t2 - (t + abs(x2 - x)))
    print(ans)

if __name__ == '__main__':
    main()