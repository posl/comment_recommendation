def main():
    N, M, Q = map(int, input().split())
    W = [0] * (N + 1)
    V = [0] * (N + 1)
    for i in range(1, N + 1):
        W[i], V[i] = map(int, input().split())
    X = list(map(int, input().split()))
    Q = [list(map(int, input().split())) for _ in range(Q)]
    for l, r in Q:
        boxes = X[:l - 1] + X[r:]
        boxes.sort()
        used = [False] * N
        ans = 0
        for b in boxes:
            idx = -1
            for i in range(N):
                if not used[i] and W[i + 1] <= b and (idx == -1 or V[idx + 1] < V[i + 1]):
                    idx = i
            if idx != -1:
                used[idx] = True
                ans += V[idx + 1]
        print(ans)

if __name__ == '__main__':
    main()