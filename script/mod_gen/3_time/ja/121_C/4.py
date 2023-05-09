def main():
    n, m = map(int, input().split())
    drink = []
    for i in range(n):
        a, b = map(int, input().split())
        drink.append((a, b))
    drink.sort()
    ans = 0
    for i in range(n):
        if m >= drink[i][1]:
            ans += drink[i][0] * drink[i][1]
            m -= drink[i][1]
        else:
            ans += drink[i][0] * m
            m -= m
        if m == 0:
            break
    print(ans)

if __name__ == '__main__':
    main()