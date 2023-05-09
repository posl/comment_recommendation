def main():
    N, M, Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    WV.sort(key=lambda x: x[1], reverse=True)
    X = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(Q)]
    for L, R in queries:
        box = X[:L-1] + X[R:]
        box.sort()
        ans = 0
        for w, v in WV:
            for i in range(len(box)):
                if box[i] >= w:
                    ans += v
                    box.pop(i)
                    break
        print(ans)

if __name__ == '__main__':
    main()