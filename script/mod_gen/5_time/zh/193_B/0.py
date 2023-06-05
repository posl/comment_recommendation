def buy_play_snuke():
    n = int(input())
    a, p, x = [], [], []
    for i in range(n):
        ai, pi, xi = map(int, input().split())
        a.append(ai)
        p.append(pi)
        x.append(xi)
    flag = 0
    min_price = 10**9
    for j in range(n):
        if x[j] > 0:
            if p[j] < min_price:
                min_price = p[j]
                flag = 1
    if flag == 0:
        return -1
    else:
        return min_price

if __name__ == '__main__':
    buy_play_snuke()