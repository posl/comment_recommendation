def p178_c():
    n = int(input())
    ans = pow(10, n, 10**9+7) - pow(9, n, 10**9+7) - pow(9, n, 10**9+7) + pow(8, n, 10**9+7)
    print(ans % (10**9+7))

if __name__ == '__main__':
    p178_c()