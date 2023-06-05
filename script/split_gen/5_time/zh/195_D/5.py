def main():
    n,m,q = map(int,input().split())
    wv = [list(map(int,input().split())) for _ in range(n)]
    x = list(map(int,input().split()))
    query = [list(map(int,input().split())) for _ in range(q)]
    ans = []
    for i in range(q):
        l,r = query[i][0],query[i][1]
        box = x[:l-1]+x[r:]
        box.sort()
        box.reverse()
        box = box[:n]
        box.sort()
        box.reverse()
        box = box[:n]
        wv.sort(key=lambda x:x[1])
        wv.reverse()
        wv = wv[:n]
        wv.sort(key=lambda x:x[0])
        wv.reverse()
        wv = wv[:n]
        wv = [i for i in wv if i[0]<=box[0]]
        wv.sort(key=lambda x:x[1])
        wv.reverse()
        wv = wv[:n]
        ans.append(sum([i[1] for i in wv]))
    for i in ans:
        print(i)
