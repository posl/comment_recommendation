def get_max_value(n, m, cakes):
    # n is the number of cakes
    # m is the number of cakes to be chosen
    # cakes is a list of cakes, each cake is a list of three integers
    # cakes[i][0] is the beauty of cake i
    # cakes[i][1] is the taste of cake i
    # cakes[i][2] is the popularity of cake i
    # return the maximum value
    # write your code here
    # 1. sort cakes by beauty
    cakes.sort(key=lambda x: x[0], reverse=True)
    # 2. split cakes into two groups
    cakes1 = cakes[:m]
    cakes2 = cakes[m:]
    # 3. sort cakes2 by taste
    cakes2.sort(key=lambda x: x[1], reverse=True)
    # 4. sort cakes2 by popularity
    cakes2.sort(key=lambda x: x[2], reverse=True)
    # 5. get the maximum value
    max_value = 0
    for cake in cakes1:
        max_value += abs(cake[0]) + abs(cake[1]) + abs(cake[2])
    for cake in cakes2:
        max_value += abs(cake[0]) + abs(cake[1]) + abs(cake[2])
    return max_value
