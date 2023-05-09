def main():
    N, M, Q = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    query = [list(map(int, input().split())) for _ in range(Q)]
    for l, r in query:
        box = X[:l-1] + X[r:]
        box.sort()
        wv.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        for w, v in wv:
            for i in range(len(box)):
                if box[i] >= w:
                    ans += v
                    box[i] = -1
                    break
        print(ans)

if __name__ == '__main__':
    main()