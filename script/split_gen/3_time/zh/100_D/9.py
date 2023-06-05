def findMaxBeauty(cakes, m):
    cakes.sort(key=lambda cake: abs(cake[0]) + abs(cake[1]) + abs(cake[2]), reverse=True)
    # print(cakes)
    # print(cakes[0][0], cakes[0][1], cakes[0][2])
    beauty = abs(cakes[0][0])
    delicious = abs(cakes[0][1])
    popularity = abs(cakes[0][2])
    for i in range(1, m):
        beauty += abs(cakes[i][0])
        delicious += abs(cakes[i][1])
        popularity += abs(cakes[i][2])
    return beauty + delicious + popularity
