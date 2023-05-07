def main():
    N, M, Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    Query = [list(map(int, input().split())) for _ in range(Q)]
    for L, R in Query:
        #print(L, R)
        boxes = X[:L-1] + X[R:]
        boxes.sort()
        #print(boxes)
        wv = WV[:]
        wv.sort(key=lambda x:x[1], reverse=True)
        #print(wv)
        ans = 0
        for w, v in wv:
            for i, b in enumerate(boxes):
                if w <= b:
                    ans += v
                    boxes[i] = 0
                    break
        print(ans)

if __name__ == '__main__':
    main()