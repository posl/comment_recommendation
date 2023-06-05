def buy_all(N,X,prices):
    total = 0
    for i in range(0,N):
        if i % 2 == 0:
            total += prices[i]
        else:
            total += prices[i] - 1
    if total <= X:
        print('Yes')
    else:
        print('No')
