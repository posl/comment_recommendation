def  main():
    N = int(input())
    #N=10**18
    #N=250
    #N=1
    #N=123456789012345
    # 素数リストを作成
    prime = [True] * (N+1)
    prime[0] = False
    prime[1] = False
    for i in range(2, int(N**0.5)+1):
        if prime[i]:
            for j in range(i*2, N+1, i):
                prime[j] = False
    primes = [i for i in range(N+1) if prime[i]]
    # 250 に似た数のリストを作成
    num = []
    for p in primes:
        if p**3 > N:
            break
        num.append(p**3)
    for p in primes:
        if p**4 > N:
            break
        num.append(p**4)
    # 結果を出力
    print(len(num))
