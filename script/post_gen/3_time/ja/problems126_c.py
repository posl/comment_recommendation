Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        cnt = 0
        while i < K:
            i *= 2
            cnt += 1
        ans += 1 / N * (1 / 2) ** cnt
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
        return
    ans = 0
    for i in range(1, N+1):
        if i >= K:
            ans += 1
            continue
        tmp = 1/N
        j = i
        while j < K:
            j *= 2
            tmp /= 2
        ans += tmp
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    win = 0
    for i in range(1, N+1):
        count = 0
        while i < K:
            i *= 2
            count += 1
        win += 1/N * (1/2)**count
    print(win)

=======
Suggestion 4

def main():
    N,K = map(int,input().split())
    ans = 0
    for i in range(1,N+1):
        if i >= K:
            ans += 1/N
        else:
            cnt = 0
            while i < K:
                i *= 2
                cnt += 1
            ans += (1/N)*(1/2)**cnt
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    if N >= K:
        print(1)
    else:
        ans = 0
        for i in range(1, N+1):
            tmp = 1/N
            tmp *= (1/2)**((i-1).bit_length())
            ans += tmp
        print(ans)

=======
Suggestion 6

def main():
    import sys
    read = sys.stdin.buffer.read
    N, K = map(int, read().split())
    if K == 1:
        print(0)
        return
    ans = 0
    for i in range(1, N+1):
        p = 1/N
        k = i
        while k < K:
            k *= 2
            p /= 2
        ans += p
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    if K==1:
        print(0)
    else:
        ans = 0
        for i in range(1, N+1):
            p = 1/N
            x = i
            while x < K:
                p /= 2
                x *= 2
            ans += p
        print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    p = 0
    for n in range(1, N+1):
        p += (1/N) * (1/2)**(1 + (K-1)//n)
    print(p)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    # N面サイコロを振って、出た目を得点とする。
    # 得点が 0 になった、もしくは K 以上になった時点でゲームが終了する。
    # このとき、得点が K 以上である場合すぬけ君の勝ち、 0 である場合すぬけ君の負けである。
    # すぬけ君が勝つ確率を求める。
    if K == 1:
        print(0)
        return
    ans = 0
    for i in range(1, N+1):
        # 1回コインを振って、表が出たら得点は 2 倍になる。
        # 裏が出たら得点は 0 になる。
        # 得点が K 以上になった時点でゲームが終了する。
        # このとき、得点が K 以上である場合すぬけ君の勝ちである。
        # すぬけ君が勝つ確率を求める。
        # 1回振って、表が出たら得点は 2 倍になる。
        # 裏が出たら得点は 0 になる。
        # 得点が K 以上になった時点でゲームが終了する。
        # このとき、得点が K 以上である場合すぬけ君の勝ちである。
        # すぬけ君が勝つ確率を求める。
        # 1回振って、表が出たら得点は 2 倍になる。
        # 裏が出たら得点は 0 になる。
        # 得点が K 以上になった時点でゲームが終了する

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    if N >= K:
        print(1)
        return
    # 1. K-1 以下の出目について、サイコロを振った時の確率を求める
    # 2. K 以上の出目について、サイコロを振った時の確率を求める
    # 3. 1. と 2. を足す
    # 4. 3. を N で割る
    # 5. 4. を 1 から引く
    # 6. 5. を出力する
    # 1.
    sum1 = 0
    for i in range(1, K):
        sum1 += (1/N) * (1/2)**i
    # 2.
    sum2 = 0
    for i in range(K, N+1):
        sum2 += (1/N) * (1/2)**i
    # 3.
    sum3 = sum1 + sum2
    # 4.
    sum4 = sum3 / N
    # 5.
    sum5 = 1 - sum4
    # 6.
    print(sum5)
