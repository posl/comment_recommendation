def solve():
    N, X = map(int, input().split())
    # レベルNバーガーの層の総数を求める
    sum = 1
    for i in range(N):
        sum = sum * 2 + 3
    # レベルNバーガーの下からX層を食べる
    cnt = 0
    while X > 0:
        if X == sum:
            # レベルNバーガーの下からX層を食べる
            cnt += 1
            break
        elif X == sum - 1:
            # レベルNバーガーの下からX層を食べる
            break
        elif X == sum - 2:
            # レベルNバーガーの下からX層を食べる
            cnt += 1
            break
        else:
            # レベルNバーガーの下からX層を食べる
            cnt += 1
            X -= 1
            sum -= 1
            # レベルN-1バーガーの下からX層を食べる
            sum -= 1
            X -= sum
            # レベルNバーガーの下からX層を食べる
            cnt += 1
            X -= 1
            sum -= 1
    print(cnt)
