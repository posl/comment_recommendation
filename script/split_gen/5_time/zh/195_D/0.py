def main():
    n,m,q = map(int,input().split())
    wv = [list(map(int,input().split())) for _ in range(n)]
    x = list(map(int,input().split()))
    query = [list(map(int,input().split())) for _ in range(q)]
    for i in range(q):
        l,r = query[i]
        y = x[:l-1]+x[r:]
        y.sort()
        ans = 0
        for j in range(n):
            for k in range(len(y)):
                if wv[j][0]<=y[k]:
                    ans += wv[j][1]
                    y.pop(k)
                    break
        print(ans)
