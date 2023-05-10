def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    ans = 0
    i = 0
    while m > 0:
        if m >= ab[i][0]:
            ans += ab[i][1]
            m -= ab[i][0]
            i += 1
        else:
            ans += m * ab[i][1]
            m = 0
    print(ans)

if __name__ == '__main__':
    main()