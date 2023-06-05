def main():
    n,m,q = map(int,input().split())
    wv = [[int(i) for i in input().split()] for _ in range(n)]
    x = [int(i) for i in input().split()]
    query = [[int(i) for i in input().split()] for _ in range(q)]
    for i in query:
        l,r = i[0],i[1]
        x_ = x[:l-1]+x[r:]
        wv_ = []
        for j in wv:
            if j[0] <= max(x_):
                wv_.append(j)
        dp = [[0 for _ in range(sum(x_)+1)] for _ in range(len(wv_)+1)]
        for k in range(1,len(wv_)+1):
            for j in range(1,sum(x_)+1):
                if j >= wv_[k-1][0]:
                    dp[k][j] = max(dp[k-1][j],dp[k-1][j-wv_[k-1][0]]+wv_[k-1][1])
                else:
                    dp[k][j] = dp[k-1][j]
        print(dp[-1][-1])

if __name__ == '__main__':
    main()