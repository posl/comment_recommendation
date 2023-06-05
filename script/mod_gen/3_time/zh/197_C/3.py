def f(n, a):
    if n == 1:
        return 0
    if n == 2:
        return a[0] ^ a[1]
    if n == 3:
        return a[0] ^ a[1] ^ a[2]
    if n == 4:
        return 0
    if n == 5:
        return a[0] ^ a[1] ^ a[2] ^ a[3] ^ a[4]
    if n == 6:
        return 0
    if n == 7:
        return a[0] ^ a[1] ^ a[2] ^ a[3] ^ a[4] ^ a[5] ^ a[6]
    if n == 8:
        return 0
    if n == 9:
        return a[0] ^ a[1] ^ a[2] ^ a[3] ^ a[4] ^ a[5] ^ a[6] ^ a[7] ^ a[8]
    if n == 10:
        return 0
    if n == 11:
        return a[0] ^ a[1] ^ a[2] ^ a[3] ^ a[4] ^ a[5] ^ a[6] ^ a[7] ^ a[8] ^ a[9] ^ a[10]
    if n == 12:
        return 0
    if n == 13:
        return a[0] ^ a[1] ^ a[2] ^ a[3] ^ a[4] ^ a[5] ^ a[6] ^ a[7] ^ a[8] ^ a[9] ^ a[10] ^ a[11] ^ a[12]
    if n == 14:
        return 0
    if n == 15:
        return a[0] ^ a[1] ^ a[2] ^ a[3] ^ a[4] ^ a[5] ^ a[6] ^ a[7] ^ a[8] ^ a[9] ^ a[10] ^ a[11] ^ a[12] ^ a[13] ^ a[14]
    if n == 16:
        return 0
    if n == 17:
        return a

if __name__ == '__main__':
    f()