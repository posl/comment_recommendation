def main():
    n, m = map(int, input().split())
    drinks = []
    for _ in range(n):
        a, b = map(int, input().split())
        drinks.append([a, b])
    drinks.sort(key=lambda x: x[0])
    ans = 0
    for drink in drinks:
        if m <= drink[1]:
            ans += drink[0] * m
            break
        else:
            ans += drink[0] * drink[1]
            m -= drink[1]
    print(ans)

if __name__ == '__main__':
    main()