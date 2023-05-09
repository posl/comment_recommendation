def main():
    n,m = map(int,input().split())
    shop = []
    for i in range(n):
        a,b = map(int,input().split())
        shop.append([a,b])
    shop.sort()
    ans = 0
    for i in range(n):
        if m <= 0:
            break
        if m >= shop[i][1]:
            ans += shop[i][0] * shop[i][1]
            m -= shop[i][1]
        else:
            ans += shop[i][0] * m
            m = 0
    print(ans)
