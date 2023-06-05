def toHexadecimal(N):
    if N < 10:
        return N
    elif N == 10:
        return 'A'
    elif N == 11:
        return 'B'
    elif N == 12:
        return 'C'
    elif N == 13:
        return 'D'
    elif N == 14:
        return 'E'
    elif N == 15:
        return 'F'
    else:
        return 0
N = int(input())
print(toHexadecimal(N // 16), end='')
print(toHexadecimal(N % 16))
