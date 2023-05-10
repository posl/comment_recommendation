def solve():
    # 入力
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 机Aで読むことができる本の冊数、所要時間
    a = 0
    t = 0
    for i in range(N):
        if t + A[i] <= K:
            a += 1
            t += A[i]
        else:
            break
    # 机Bで読むことができる本の冊数、所要時間
    b = 0
    t = 0
    for i in range(M):
        if t + B[i] <= K:
            b += 1
            t += B[i]
        else:
            break
    # 机Aと机Bのそれぞれで読むことができる本の冊数の合計の最大値を求める
    ans = a + b
    # 机Aの上からi冊目までの本を読んだ時の所要時間
    t = 0
    for i in range(N):
        # 机Aの上からi冊目までの本を読んだ時の所要時間
        t += A[i]
        # 机Bで読むことができる本の冊数
        b = 0
        for j in range(M):
            # 机Bの上からj冊目までの本を読んだ時の所要時間
            t += B[j]
            # 机Bで読むことができる本の冊数
            if t > K:
                break
            b += 1
        # 机Aと机Bのそれぞれで読むことができる本の冊数の合計の最大値を更新する
        ans = max(ans, i + 1 + b)
    print(ans)

if __name__ == '__main__':
    solve()