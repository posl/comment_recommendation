def getNumber(n):
    if n == 0:
        return "0"
    result = ""
    while n != 0:
        if n % 2 == 0:
            result = "0" + result
            n = n // (-2)
        else:
            result = "1" + result
            n = (n - 1) // (-2)
    return result
n = int(input())
print(getNumber(n))
