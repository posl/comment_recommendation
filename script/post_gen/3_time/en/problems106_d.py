Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]

    # 1. LRを左端でソートする
    # 2. PQを左端でソートする
    # 3. LRを左端がPQの左端以降のものを抽出し、右端でソートする
    # 4. LRを右端がPQの右端以前のものを抽出する
    # 5. LRを右端でソートする
    # 6. LRを右端がPQの左端以降のものを抽出する
    # 7. LRの長さを出力する
    LR = sorted(LR, key=lambda x: x[0])
    PQ = sorted(PQ, key=lambda x: x[0])
    LR = sorted([lr for lr in LR if lr[0] >= PQ[0][0]], key=lambda x: x[1])
    LR = [lr for lr in LR if lr[1] <= PQ[0][1]]
    LR = sorted(LR, key=lambda x: x[1])
    LR = [lr for lr in LR if lr[1] >= PQ[0][0]]
    print(len(LR))

=======
Suggestion 2

def main():
    N, M, Q = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    p = [0] * Q
    q = [0] * Q
    for i in range(Q):
        p[i], q[i] = map(int, input().split())
    for i in range(Q):
        count = 0
        for j in range(M):
            if p[i] <= L[j] and R[j] <= q[i]:
                count += 1
        print(count)

=======
Suggestion 3

def main():
    N, M, Q = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    p = [0] * Q
    q = [0] * Q
    for i in range(Q):
        p[i], q[i] = map(int, input().split())
    for i in range(Q):
        count = 0
        for j in range(M):
            if L[j] < p[i] or q[i] < R[j]:
                continue
            elif L[j] == p[i] and R[j] == q[i]:
                continue
            else:
                count += 1
        print(count)

=======
Suggestion 4

def main():
    N, M, Q = map(int, input().split())
    trains = [list(map(int, input().split())) for _ in range(M)]
    queries = [list(map(int, input().split())) for _ in range(Q)]
    for q in queries:
        print(sum([1 for t in trains if q[0] <= t[0] and t[1] <= q[1]]))

=======
Suggestion 5

def main():
    n, m, q = map(int, input().split())
    train = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        l, r = map(int, input().split())
        train[l][r] += 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            train[i][j] += train[i][j - 1]
    for _ in range(q):
        p, q = map(int, input().split())
        ans = 0
        for i in range(p, q + 1):
            ans += train[i][q] - train[i][p - 1]
        print(ans)

=======
Suggestion 6

def main():
    N, M, Q = map(int, input().split())
    trains = []
    for i in range(M):
        L, R = map(int, input().split())
        trains.append((L, R))
    queries = []
    for i in range(Q):
        p, q = map(int, input().split())
        queries.append((p, q))
    for p, q in queries:
        ans = 0
        for L, R in trains:
            if p <= L and R <= q:
                ans += 1
        print(ans)

=======
Suggestion 7

def main():
    N, M, Q = map(int, input().split())
    trains = [set() for _ in range(N)]
    for _ in range(M):
        L, R = map(int, input().split())
        trains[L-1].add(R)
    for i in range(1, N):
        trains[i] |= trains[i-1]
    for _ in range(Q):
        p, q = map(int, input().split())
        print(len(trains[q-1] & set(range(p, q))))

=======
Suggestion 8

def main():
    N, M, Q = map(int, input().split())

    train = [[0] * (N + 1) for i in range(N + 1)]
    for i in range(M):
        L, R = map(int, input().split())
        train[L][R] += 1

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            train[i][j] += train[i - 1][j] + train[i][j - 1] - train[i - 1][j - 1]

    for i in range(Q):
        p, q = map(int, input().split())
        print(train[q][q] - train[q][p - 1] - train[p - 1][q] + train[p - 1][p - 1])

=======
Suggestion 9

def read_ints():
    return list(map(int, input().split()))
