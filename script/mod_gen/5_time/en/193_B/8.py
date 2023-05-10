def solve():
    N = int(input())
    shops = [list(map(int, input().split())) for _ in range(N)]
    min_price = float('inf')
    for shop in shops:
        if shop[2] > shop[0]:
            min_price = min(min_price, shop[1])
    if min_price == float('inf'):
        print(-1)
    else:
        print(min_price)

if __name__ == '__main__':
    solve()