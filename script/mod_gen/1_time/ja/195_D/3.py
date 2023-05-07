def main():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    for _ in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    X = list(map(int, input().split()))
    for _ in range(Q):
        L, R = map(int, input().split())
        #print(L, R)
        #箱を選ぶ
        box = X[:L-1] + X[R:]
        #print(box)
        #荷物を選ぶ
        wv = [[W[i], V[i]] for i in range(N)]
        #print(wv)
        #価値の高い順にソート
        wv.sort(key=lambda x: x[1], reverse=True)
        #print(wv)
        #箱に入れる
        ans = 0
        for w, v in wv:
            #print(w, v)
            for i in range(len(box)):
                if box[i] >= w:
                    ans += v
                    box[i] = 0
                    break
        print(ans)

if __name__ == '__main__':
    main()