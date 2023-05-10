def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    ans = 0
    for a, b in ab:
        if m >= a:
            ans += b
            m -= a
        else:
            ans += b * m
            break
    print(ans)

if __name__ == '__main__':
    main()