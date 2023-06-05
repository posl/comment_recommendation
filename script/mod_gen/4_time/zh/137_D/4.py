def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    ans = 0
    for i in range(n):
        if m > ab[i][0]:
            m -= ab[i][0]
            ans += ab[i][1]
        else:
            ans += ab[i][1] * m
            break
    print(ans)

if __name__ == '__main__':
    main()