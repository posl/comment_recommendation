def main():
    S = input()
    Q = S.count("?")
    A = S.count("A")
    B = S.count("B")
    C = S.count("C")
    ans = 0
    for i in range(Q+1):
        for j in range(Q+1-i):
            k = Q - i - j
            ans += (pow(3, i, 10**9+7) * pow(3, j, 10**9+7) * pow(3, k, 10**9+7) * (A+i) * (B+j) * (C+k))
    print(ans % (10**9+7))

if __name__ == '__main__':
    main()