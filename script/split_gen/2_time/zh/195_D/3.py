def main():
    n,m,q = map(int,input().split())
    wv = [list(map(int,input().split())) for _ in range(n)]
    x = list(map(int,input().split()))
    query = [list(map(int,input().split())) for _ in range(q)]
    for l,r in query:
        box = x[:l-1]+x[r:]
        box.sort()
        box.reverse()
        ans = 0
        for w,v in wv:
            for i in range(len(box)):
                if box[i] >= w:
                    ans += v
                    box.pop(i)
                    break
        print(ans)
