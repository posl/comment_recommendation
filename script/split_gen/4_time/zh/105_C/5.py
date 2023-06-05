def convertToBaseNeg2(N):
    if (N == 0):
        return '0'
    ans = ''
    while (N != 0):
        rem = N % (-2)
        N = N // (-2)
        if (rem < 0):
            rem += 2
            N += 1
        ans = str(rem) + ans
    return ans
N = int(input())
print(convertToBaseNeg2(N))
