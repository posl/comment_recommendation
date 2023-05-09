def main():
    N = int(input())
    if N == 1:
        print(0)
        exit()
    #Nを素因数分解
    prime_factor = {}
    for i in range(2, int(N**0.5)+1):
        while N % i == 0:
            if i in prime_factor:
                prime_factor[i] += 1
            else:
                prime_factor[i] = 1
            N //= i
    if N != 1:
        if N in prime_factor:
            prime_factor[N] += 1
        else:
            prime_factor[N] = 1
    #print(prime_factor)
    #print(prime_factor)
    #素因数の数を求める
    prime_factor_num = 0
    for i in prime_factor:
        prime_factor_num += prime_factor[i]
    #print(prime_factor_num)
    #素因数の数を用いて約数の数を求める
    divisor_num = 1
    for i in prime_factor:
        divisor_num *= prime_factor[i]+1
    #print(divisor_num)
    #約数の数-1を出力
    print(divisor_num-1)

if __name__ == '__main__':
    main()