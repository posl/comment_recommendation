def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x:x[0])
    ans = 0
    cnt = 0
    for a, b in ab:
        if cnt + a <= m:
            cnt += a
            ans += b
        else:
            ans += (m - cnt) * b
            break
    print(ans)

if __name__ == '__main__':
    main()