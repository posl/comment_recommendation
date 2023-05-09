def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 1からの距離を求める
    dist = [0] * (N+1)
    dist[1] = 1
    q = [1]
    while len(q) > 0:
        p = q.pop()
        for i in range(M):
            if A[i] == p and dist[B[i]] == 0:
                dist[B[i]] = dist[p] + 1
                q.append(B[i])
            if B[i] == p and dist[A[i]] == 0:
                dist[A[i]] = dist[p] + 1
                q.append(A[i])
    # 1から最も遠いところを求める
    d = 0
    for i in range(2, N+1):
        d = max(d, dist[i])
    # 1から最も遠いところの候補を求める
    cands = []
    for i in range(2, N+1):
        if dist[i] == d:
            cands.append(i)
    # 候補から選ぶ
    q = cands
    for _ in range(d-1):
        q2 = []
        for p in q:
            for i in range(M):
                if A[i] == p and dist[B[i]] == d-1:
                    q2.append(B[i])
                if B[i] == p and dist[A[i]] == d-1:
                    q2.append(A[i])
        q = q2
        d -= 1
    # 答えを求める
    ans = [''] * (N+1)
    for i in range(len(q)):
        ans[q[i]] = cands[i]
    print('Yes')
    for a in ans[2:]:
        print(a)
main()

if __name__ == '__main__':
    main()