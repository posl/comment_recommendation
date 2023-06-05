def main():
    n = int(input())
    a = []
    p = []
    x = []
    for i in range(n):
        a_i, p_i, x_i = map(int, input().split())
        a.append(a_i)
        p.append(p_i)
        x.append(x_i)
    min_price = 10**9 + 1
    for i in range(n):
        if x[i] > 0:
            if p[i] < min_price:
                min_price = p[i]
    if min_price == 10**9 + 1:
        print(-1)
    else:
        print(min_price)
