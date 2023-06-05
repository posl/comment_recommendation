def main():
    # n,m,x = map(int,input().split())
    # c_a = []
    # for i in range(n):
    #     c_a.append(list(map(int,input().split())))
    n,m,x = 3,3,10
    c_a = [[60,2,2,4],[70,8,7,9],[50,2,3,9]]
    # n,m,x = 3,3,10
    # c_a = [[100,3,1,4],[100,1,5,9],[100,2,6,5]]
    # n,m,x = 8,5,22
    # c_a = [[100,3,7,5,3,1],[164,4,5,2,7,8],[334,7,2,7,2,9],[234,4,7,2,8,2],[541,5,4,3,3,6],[235,4,8,6,9,7],[394,3,6,1,6,2],[872,8,4,3,7,2]]
    min_price = 100000000
    for i in range(2**n):
        total_price = 0
        total_a = [0]*m
        for j in range(n):
            if i & (1<<j):
                total_price += c_a[j][0]
                for k in range(m):
                    total_a[k] += c_a[j][k+1]
        if min(total_a) >= x and total_price < min_price:
            min_price = total_price
    if min_price == 100000000:
        print(-1)
    else:
        print(min_price)
