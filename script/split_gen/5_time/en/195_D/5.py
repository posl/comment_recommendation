def main():
    n,m,q = map(int,input().split())
    wv = [list(map(int,input().split())) for _ in range(n)]
    x = list(map(int,input().split()))
    queries = [list(map(int,input().split())) for _ in range(q)]
    for i in range(q):
        l,r = queries[i]
        boxes = x[:l-1] + x[r:]
        boxes.sort()
        #print(boxes)
        tmp = 0
        for j in range(n):
            for k in range(len(boxes)):
                if wv[j][0] <= boxes[k]:
                    tmp += wv[j][1]
                    boxes.pop(k)
                    break
        print(tmp)
