def solve():
    n,m,q = map(int,input().split())
    wv = [list(map(int,input().split())) for _ in range(n)]
    x = list(map(int,input().split()))
    query = [list(map(int,input().split())) for _ in range(q)]
    for i in range(q):
        l,r = query[i]
        box = x[:l-1] + x[r:]
        box.sort()
        ans = 0
        for j in range(n):
            if len(box) == 0:
                break
            for k in range(len(box)):
                if wv[j][0] <= box[k]:
                    ans += wv[j][1]
                    box.pop(k)
                    break
        print(ans)
    return 0
