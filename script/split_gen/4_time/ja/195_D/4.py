def main():
    n,m,q = map(int,input().split())
    wv = [list(map(int,input().split())) for _ in range(n)]
    x = list(map(int,input().split()))
    query = [list(map(int,input().split())) for _ in range(q)]
    for i in range(q):
        l,r = query[i]
        boxes = x[:l-1] + x[r:]
        boxes.sort()
        ans = 0
        for j in range(n):
            tmp = 0
            for k in range(len(boxes)):
                if wv[j][0] <= boxes[k]:
                    if tmp < wv[j][1]:
                        tmp = wv[j][1]
            ans += tmp
        print(ans)
