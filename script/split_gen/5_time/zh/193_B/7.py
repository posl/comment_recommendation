def buyPlaySnuke(n):
    minPrice = -1
    for i in range(n):
        a, p, x = map(int, input().split())
        if x > 0:
            if minPrice == -1:
                minPrice = p
            elif minPrice > p:
                minPrice = p
    print(minPrice)
