def main():
    N = int(input())
    A = list(map(int,input().split()))
    mod = 998244353
    #nCkを求める関数
    def combination(n,k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        a = 1
        b = 1
        for i in range(k):
            a = a * (n - i) % mod
            b = b * (i + 1) % mod
        return a * pow(b,mod-2,mod) % mod
    #Aの項を選ぶ方法それぞれに対する平均値が整数となるものの通り数を求める
    ans = 0
    for i in range(N):
        #Aのi番目の項を選ぶ場合
        ans += combination(N-1,i) * A[i]
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()