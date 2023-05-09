def base_m(N, m):
    if N == 0:
        return '0'
    elif N < 0:
        N = -N
        minus = True
    else:
        minus = False
    ans = ''
    while N > 0:
        ans = str(N % m) + ans
        N //= m
    if minus:
        ans = '-' + ans
    return ans

if __name__ == '__main__':
    base_m()