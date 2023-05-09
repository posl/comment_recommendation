def main():
    N = int(input())
    #素数のリスト
    prime_list = []
    #素因数分解
    for i in range(2, int(N**0.5)+1):
        while N%i == 0:
            prime_list.append(i)
            N //= i
    if N > 1:
        prime_list.append(N)
    #print(prime_list)
    #print(len(prime_list))
    #素因数分解の結果のリストの中で、最大の数を出力
    print(len(prime_list))

if __name__ == '__main__':
    main()