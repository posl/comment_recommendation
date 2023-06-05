def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    m = 2 * 10 ** 5 + 1
    for i in range(n):
        if p[i] < m:
            ans += 1
            m = p[i]
    print(ans)

if __name__ == '__main__':
    main()