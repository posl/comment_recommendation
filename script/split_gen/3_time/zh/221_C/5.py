def maxProduct(n):
    n = str(n)
    if len(n) == 2:
        return int(n[0]) * int(n[1])
    else:
        maxProduct = 0
        for i in range(1, len(n)):
            a = int(n[:i])
            b = int(n[i:])
            if a * b > maxProduct:
                maxProduct = a * b
        return maxProduct
