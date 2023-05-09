def baseNeg2(N):
    if N == 0:
        return '0'
    ans = ''
    while N != 0:
        ans = str(N & 1) + ans
        N = -(N >> 1)
    return ans
N = int(input())
print(baseNeg2(N))
