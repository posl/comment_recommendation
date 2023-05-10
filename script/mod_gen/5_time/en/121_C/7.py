def main():
    n, m = map(int, input().split())
    drink = []
    for i in range(n):
        drink.append(list(map(int, input().split())))
    drink.sort()
    ans = 0
    for i in range(n):
        if drink[i][1] >= m:
            ans += drink[i][0] * m
            break
        else:
            ans += drink[i][0] * drink[i][1]
            m -= drink[i][1]
    print(ans)

if __name__ == '__main__':
    main()