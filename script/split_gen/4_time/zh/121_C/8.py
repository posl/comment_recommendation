def main():
    n,m = map(int,input().split())
    shop = []
    for i in range(n):
        a,b = map(int,input().split())
        shop.append([a,b])
    shop.sort()
    sum = 0
    for s in shop:
        if m <= s[1]:
            sum += m * s[0]
            break
        else:
            sum += s[1] * s[0]
            m -= s[1]
    print(sum)
