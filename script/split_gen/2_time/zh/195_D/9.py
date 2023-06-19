def main():
    n,m,q = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(n)]
    x = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(q)]
    ans = [0] * q
    for i in range(q):
        l, r = queries[i]
        boxes = x[:l-1] + x[r:]
        boxes.sort()
        boxes = boxes[::-1]
        boxes = boxes[:n]
        boxes.sort()
        boxes = boxes[::-1]
        boxes = boxes[:n]
        wv.sort(key=lambda x:x[1], reverse=True)
        for j in range(n):
            for k in range(n):
                if wv[k][0] <= boxes[j]:
                    ans[i] += wv[k][1]
                    wv[k][0] = 10**9
                    break
    for i in range(q):
        print(ans[i])
