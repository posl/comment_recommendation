def getMinPrice(n, m, stores):
    # stores.sort(key = lambda x: x[0]/x[1])
    # print(stores)
    stores.sort(key = lambda x: x[0])
    # print(stores)
    # print(stores[0][0])
    # print(stores[0][1])
    count = 0
    price = 0
    for i in range(n):
        if count >= m:
            break
        if count + stores[i][1] >= m:
            price += (m - count) * stores[i][0]
            count += (m - count)
        else:
            price += stores[i][1] * stores[i][0]
            count += stores[i][1]
    return price
