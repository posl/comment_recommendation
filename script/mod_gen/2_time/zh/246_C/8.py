def buy(n, k, x, a):
    cost = 0
    for i in range(n):
        if a[i] > x:
            cost += a[i] - x
    cost = min(cost, k)
    return cost

if __name__ == '__main__':
    buy()