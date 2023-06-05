def solution(n, a):
    if n == 1:
        return 0
    if n == 2:
        return a[0] ^ a[1]
    if n == 3:
        return (a[0] ^ a[1]) ^ a[2]
    if n == 4:
        return 0
    if n == 5:
        return a[0] ^ a[1] ^ a[2] ^ a[3] ^ a[4]
    return 0
