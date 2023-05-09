def solve():
    n, m = map(int, input().split())
    drinks = []
    for i in range(n):
        a, b = map(int, input().split())
        drinks.append((a, b))
    drinks.sort()
    count = 0
    price = 0
    for drink in drinks:
        if count + drink[1] <= m:
            count += drink[1]
            price += drink[0] * drink[1]
        else:
            price += drink[0] * (m - count)
            break
    print(price)

if __name__ == '__main__':
    solve()