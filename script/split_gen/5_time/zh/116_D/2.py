def solve():
    N, K = map(int, input().split())
    sushi = [list(map(int, input().split())) for _ in range(N)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    # 1. 一番美味しいものから順に，ネタの種類で分ける
    # 2. 各ネタの中で，一番美味しいものを選ぶ
    # 3. 各ネタの中で，二番目に美味しいものを選ぶ
    # 4. それ以降は，一番美味しいものを選ぶ
    # 5. 1~4を繰り返す
    # 6. 最後に，ネタの種類の数だけ，ネタの種類の数を加算する
    # 7. 6で得られた値が，最大のものを選ぶ
    # 1. 一番美味しいものから順に，ネタの種類で分ける
    sushi_by_t = [[] for _ in range(N + 1)]
    for t, d in sushi:
        sushi_by_t[t].append(d)
    # 2. 各ネタの中で，一番美味しいものを選ぶ
    sushi_by_t2 = [None for _ in range(N + 1)]
    for t in range(1, N + 1):
        if len(sushi_by_t[t]) == 0:
            continue
        sushi_by_t[t].sort(reverse=True)
        sushi_by_t2[t] = sushi_by_t[t][0]
    # 3. 各ネタの中で，二番目に美味しいものを選ぶ
    sushi_by_t3 = [None for _ in range(N + 1)]
    for t in range(1, N + 1):
        if len(sushi_by_t[t]) <= 1:
            continue
        sushi_by_t[t].sort(reverse=True)
