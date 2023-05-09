def main():
    N = int(input())
    #素数の数
    cnt = 0
    #素数リスト
    prime = []
    #素数フラグ
    isPrime = [True] * (N + 1)
    #2からNまでの素数を列挙
    for i in range(2, N + 1):
        if isPrime[i]:
            cnt += 1
            prime.append(i)
            for j in range(i + i, N + 1, i):
                isPrime[j] = False
    #素数のリストの中から3乗の要素を列挙
    prime3 = []
    for i in range(cnt):
        if prime[i] ** 3 <= N:
            prime3.append(prime[i] ** 3)
    #素数のリストの中から5乗の要素を列挙
    prime5 = []
    for i in range(cnt):
        if prime[i] ** 5 <= N:
            prime5.append(prime[i] ** 5)
    #素数のリストの中から7乗の要素を列挙
    prime7 = []
    for i in range(cnt):
        if prime[i] ** 7 <= N:
            prime7.append(prime[i] ** 7)
    #素数のリストの中から9乗の要素を列挙
    prime9 = []
    for i in range(cnt):
        if prime[i] ** 9 <= N:
            prime9.append(prime[i] ** 9)
    #素数のリストの中から11乗の要素を列挙
    prime11 = []
    for i in range(cnt):
        if prime[i] ** 11 <= N:
            prime11.append(prime[i] ** 11)
    #素数のリストの中から13乗の要素を列挙
    prime13 = []
    for i in range(cnt):
        if prime[i] ** 13 <= N:
            prime13.append(prime[i] ** 13)
    #素数のリストの中から15乗の要素を列挙
    prime15 = []
    for i in range(cnt):
        if prime[i] ** 15

if __name__ == '__main__':
    main()