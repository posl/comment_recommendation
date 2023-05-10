def main():
    n, m = map(int, input().split())
    drinks = []
    for i in range(n):
        a, b = map(int, input().split())
        drinks.append((a, b))
    drinks.sort()
    ans = 0
    for i in range(n):
        if drinks[i][1] >= m:
            ans += drinks[i][0] * m
            break
        else:
            ans += drinks[i][0] * drinks[i][1]
            m -= drinks[i][1]
    print(ans)

if __name__ == '__main__':
    main()