def main():
    n,m = map(int,input().split())
    price = []
    for i in range(n):
        a,b = map(int,input().split())
        price.append([a,b])
    price.sort()
    #print(price)
    total = 0
    for i in range(n):
        if m >= price[i][1]:
            total += price[i][0] * price[i][1]
            m -= price[i][1]
        else:
            total += price[i][0] * m
            m = 0
    print(total)

if __name__ == '__main__':
    main()