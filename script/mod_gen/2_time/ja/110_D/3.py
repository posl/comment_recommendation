def main():
    N, M = map(int, input().split())
    #Mの素因数分解
    factorization = {}
    for i in range(2, int(M**0.5)+1):
        while M % i == 0:
            if i in factorization:
                factorization[i] += 1
            else:
                factorization[i] = 1
            M //= i
    if M > 1:
        factorization[M] = 1
    #約数の個数
    ans = 1
    for i in factorization.values():
        ans *= (i + 1)
        ans %= 10**9 + 7
    #N個から選ぶ
    for i in range(N):
        ans *= (i + 1)
        ans %= 10**9 + 7
    print(ans)

if __name__ == '__main__':
    main()