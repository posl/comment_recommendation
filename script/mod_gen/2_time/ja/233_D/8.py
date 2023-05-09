def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N,K,A)
    #print("A =",A)
    #print("K =",K)
    #print("N =",N)
    
    # 累積和を求める
    s = [0]
    for i in range(N):
        s.append(s[i] + A[i])
    #print("s =",s)
    
    # 累積和の差分を求める
    d = {}
    for i in range(N+1):
        #print("s[i] =",s[i])
        #print("K =",K)
        #print("s[i]-K =",s[i]-K)
        if s[i]-K in d:
            d[s[i]-K] += 1
        else:
            d[s[i]-K] = 1
    #print("d =",d)
    
    # 答えを求める
    ans = 0
    for i in range(N+1):
        #print("d[s[i]] =",d[s[i]])
        ans += d[s[i]]
        #print("ans =",ans)
    print(ans)

if __name__ == '__main__':
    main()