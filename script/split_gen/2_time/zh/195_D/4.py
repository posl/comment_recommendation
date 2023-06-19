def main():
    n,m,q = map(int,input().split())
    wv = [list(map(int,input().split())) for _ in range(n)]
    x = list(map(int,input().split()))
    query = [list(map(int,input().split())) for _ in range(q)]
    ans = []
    for L,R in query:
        box = x[:L-1]+x[R:]
        box.sort()
        wv.sort(key=lambda x: x[1],reverse=True)
        res = 0
        for i in range(n):
            for j in range(len(box)):
                if wv[i][0]<=box[j]:
                    res += wv[i][1]
                    box.pop(j)
                    break
        ans.append(res)
    for i in ans:
        print(i)
