def main():
    N, M = map(int, input().split())
    mod = 10**9 + 7
    #Mの素因数分解
    prime_factorization = {}
    i = 2
    while i*i <= M:
        while M%i == 0:
            if i in prime_factorization:
                prime_factorization[i] += 1
            else:
                prime_factorization[i] = 1
            M //= i
        i += 1
    if M != 1:
        prime_factorization[M] = 1
    #print(prime_factorization)
    #約数の個数の計算
    answer = 1
    for key, value in prime_factorization.items():
        answer *= (value + 1) * N - value + 1
        answer %= mod
    print(answer)

if __name__ == '__main__':
    main()