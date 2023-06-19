def main():
    s = input()
    q = s.count('?')
    # calculate a, b, c
    a = s.count('A')
    b = s.count('B')
    c = s.count('C')
    # calculate 3^q
    ans = pow(3, q, 10**9+7)
    # calculate ans
    for i in range(q+1):
        for j in range(q+1-i):
            k = q - i - j
            tmp = pow(3, i, 10**9+7) * pow(3, j, 10**9+7) * pow(3, k, 10**9+7)
            tmp = tmp * a * b * c
            ans += tmp
            ans %= 10**9+7
    print(ans)

if __name__ == '__main__':
    main()