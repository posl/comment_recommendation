def main():
    N, M, Q = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    query = [list(map(int, input().split())) for _ in range(Q)]
    for L, R in query:
        box = X[:L - 1] + X[R:]
        box.sort()
        wv.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        for w, v in wv:
            for i in range(len(box)):
                if box[i] >= w:
                    ans += v
                    box[i] = 0
                    break
        print(ans)

if __name__ == '__main__':
    main()