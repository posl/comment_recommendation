def main():
    n = int(input())
    stock = [list(map(int, input().split())) for _ in range(n)]
    stock.sort()
    for i in range(n):
        if stock[i][2] - stock[i][0] > 0:
            print(stock[i][1])
            return
    print(-1)
