def main():
    n, m = map(int, input().split())
    shops = []
    for i in range(n):
        a, b = map(int, input().split())
        shops.append((a, b))
    shops.sort(key=lambda x: x[0])
    count = 0
    money = 0
    for i in range(n):
        if count + shops[i][1] < m:
            money += shops[i][0] * shops[i][1]
            count += shops[i][1]
        else:
            money += shops[i][0] * (m - count)
            count = m
            break
    print(money)
