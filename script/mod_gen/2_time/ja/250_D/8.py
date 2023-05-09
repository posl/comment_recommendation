def main():
    N = int(input())
    #素数のリストを作成
    #Nの平方根まで見れば十分
    #素数のリストを作成
    #Nの平方根まで見れば十分
    prime = [True] * (int(N**0.5)+1)
    prime[0], prime[1] = False, False
    for i in range(2, int(N**0.5)+1):
        if prime[i]:
            for j in range(i*2, int(N**0.5)+1, i):
                prime[j] = False
    #素数のリストから素数のみ抜き出し
    prime_list = [i for i, x in enumerate(prime) if x]
    #素数のリストから素数のみ抜き出し
    prime_list = [i for i, x in enumerate(prime) if x]
    #素数のリストを使って、N以下の「 250 に似た数」をカウント
    #素数のリストを使って、N以下の「 250 に似た数」をカウント
    count = 0
    for i in prime_list:
        for j in range(1, int(N**0.25)+1):
            if i * j**3 <= N:
                count += 1
    print(count)

if __name__ == '__main__':
    main()