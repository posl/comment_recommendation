def main():
    n,m = map(int,input().split())
    price_1 = []
    price_2 = []
    for i in range(n):
        a,b = map(int,input().split())
        price_1.append(a)
        price_2.append(b)
    price_1 = sorted(price_1)
    price_2 = sorted(price_2)
    sum = 0
    for i in range(m):
        if price_2[0] > price_1[i]:
            sum += price_1[i]
        else:
            sum += price_2[0]
    print(sum)
