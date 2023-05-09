def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #最大公約数を求める関数
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    #最大公約数を求める
    g = A[0]
    for i in range(1, N):
        g = gcd(g, A[i])
    #print(g)
    #最大公約数の倍数を求める
    ans = []
    for i in range(1, 1000):
        if g % i == 0:
            ans.append(i)
    #print(ans)
    #最大公約数の倍数のうち、Aの要素に含まれるものを求める
    ans2 = []
    for i in ans:
        for j in A:
            if j % i == 0:
                ans2.append(i)
                break
    #print(ans2)
    #最大公約数の倍数のうち、Aの要素に含まれるもののうち、最大のものを求める
    ans3 = ans2[0]
    for i in ans2:
        if ans3 < i:
            ans3 = i
    #print(ans3)
    print(ans3)

if __name__ == '__main__':
    main()