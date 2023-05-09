def main():
    n,m,k = map(int,input().split())
    ab = [list(map(int,input().split())) for i in range(m)]
    cd = [list(map(int,input().split())) for i in range(k)]
    #友達関係のグラフを作る
    friend = [[] for i in range(n)]
    for i in range(m):
        a,b = ab[i][0],ab[i][1]
        friend[a-1].append(b-1)
        friend[b-1].append(a-1)
    #ブロック関係のグラフを作る
    block = [[] for i in range(n)]
    for i in range(k):
        c,d = cd[i][0],cd[i][1]
        block[c-1].append(d-1)
        block[d-1].append(c-1)
    #友達候補の数を求める
    for i in range(n):
        ans = len(friend[i]) - 1
        for j in friend[i]:
            if j in block[i]:
                ans -= 1
        print(ans,end=" ")

if __name__ == '__main__':
    main()