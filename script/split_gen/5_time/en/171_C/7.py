def convertToBase26(n):
    result = ''
    while n > 0:
        n -= 1
        result = chr(n % 26 + 97) + result
        n //= 26
    return result
N = int(input())
print(convertToBase26(N))
