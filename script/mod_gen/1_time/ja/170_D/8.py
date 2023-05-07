def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 重複を取り除く
    a = list(set(a))
    a.sort()
    # 素数のリストを作る
    prime = [True] * (10**6 + 1)
    prime[0] = False
    prime[1] = False
    for i in range(2, int((10**6 + 1)**0.5) + 1):
        if prime[i]:
            for j in range(i * 2, 10**6 + 1, i):
                prime[j] = False
    # 素因数分解
    def prime_factorize(n):
        arr = []
        temp = n
        for i in range(2, int(n**0.5) + 1):
            if temp % i == 0:
                cnt = 0
                while temp % i == 0:
                    cnt += 1
                    temp //= i
                arr.append([i, cnt])
        if temp != 1:
            arr.append([temp, 1])
        if arr == []:
            arr.append([n, 1])
        return arr
    # 素数のリストを作る
    prime = [True] * (10**6 + 1)
    prime[0] = False
    prime[1] = False
    for i in range(2, int((10**6 + 1)**0.5) + 1):
        if prime[i]:
            for j in range(i * 2, 10**6 + 1, i):
                prime[j] = False
    # 素因数分解
    def prime_factorize(n):
        arr = []
        temp = n
        for i in range(2, int(n**0.5) + 1):
            if temp % i == 0:
                cnt = 0
                while temp % i == 0:
                    cnt += 1
                    temp //= i
                arr.append([i, cnt])
        if temp != 1:
            arr.append([temp, 1])
        if arr == []:
            arr.append([n, 1])
        return arr
    # 素因数分解したも

if __name__ == '__main__':
    main()