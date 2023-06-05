def getBinary(n):
    result = []
    while n > 0:
        result.append(n % 2)
        n //= 2
    return result
