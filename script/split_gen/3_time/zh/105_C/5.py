def convertToBaseNeg2(n):
    if n == 0:
        return '0'
    res = ''
    while n != 0:
        res = str(n&1) + res
        n = -(n>>1)
    return res
n = int(input())
print(convertToBaseNeg2(n))
