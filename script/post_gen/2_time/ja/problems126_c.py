Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,K = map(int,input().split())
    ans = 0
    for i in range(1,N+1):
        cnt = 0
        while i<K:
            i *= 2
            cnt += 1
        ans += 1/N * (1/2)**cnt
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        if i >= K:
            ans += 1
        else:
            j = i
            while j < K:
                j *= 2
                ans += 1/N
    print(ans/N)

=======
Suggestion 3

def main():
    N,K = map(int,input().split())
    ans = 0
    for i in range(1,N+1):
        score = i
        cnt = 0
        while score < K:
            score *= 2
            cnt += 1
        ans += 1/N * (1/2)**cnt
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        cnt = 1 / n
        tmp = i
        while tmp < k:
            tmp *= 2
            cnt /= 2
        ans += cnt
    print(ans)

=======
Suggestion 5

def main():
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        j = i
        c = 0
        while j < K:
            j *= 2
            c += 1
        ans += (1/N) * (1/2)**c
    print(ans)

=======
Suggestion 6

def main():

    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n + 1):
        cnt = 0
        x = i
        while x < k:
            x *= 2
            cnt += 1
        ans += 1 / n * (1/2) ** cnt
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    if N < K:
        print((1/N) * ((1/2)**(int(math.log(K, 2)))))
    else:
        print(1 - ((N-K+1)/N))

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    # 確率
    prob = 0
    # 1からNまでの確率を計算
    for i in range(1, N + 1):
        # サイコロの目
        dice = i
        # 確率
        p = 1 / N
        # サイコロの目がK未満の場合
        while dice < K:
            # コインを振り、表が出たら2倍になる
            dice *= 2
            # コインの確率
            p *= 0.5
        # 確率を足す
        prob += p
    # 確率を出力
    print(prob)

=======
Suggestion 9

def main():
    n,k=map(int,input().split())
    #n=サイコロの面数
    #k=勝利条件
    #勝利条件を満たす確率
    #勝利条件を満たす確率は、サイコロの出る目がk以上の時の確率
    #サイコロの出る目がk以上の時の確率は、k以上になるまでコインを振る確率の和
    #k以上になるまでコインを振る確率は、コインを振る回数の確率の和
    #コインを振る回数の確率は、コインを振る回数が1回の確率+コインを振る回数が2回の確率+・・・+コインを振る回数がk-1回の確率
    #コインを振る回数が1回の確率は、コインが表の確率*コインが裏の確率*・・・*コインが表の確率
    #コインが表の確率は、1/2
    #コインを振る回数が2回の確率は、コインが表の確率*コインが裏の確率*・・・*コインが表の確率
    #コインが表の確率は、1/2
    #コインを振る回数がk-1回の確率は、コインが表の確率*コインが裏の確率*・・・*コインが表の確率
    #コインが表の確率は、1/2
    #勝利条件を満たす確率は、サイコロの出る目がk以上の時の確率
    #サイコロの出る目がk以上の時の確率は、k以上になるまでコインを振る確率の和
    #k以上

=======
Suggestion 10

def main():
    N,K = map(int,input().split())
    # 期待値を計算する
    # 1. サイコロの出た目が1のとき
    # 2. サイコロの出た目が2のとき
    # 3. サイコロの出た目が3のとき
    # 4. サイコロの出た目が4のとき
    # 5. サイコロの出た目が5のとき
    # 6. サイコロの出た目が6のとき
    # 1,2,3,4,5,6の期待値の合計が勝率
    # 1. サイコロの出た目が1のとき
    # 1/6 * 1/2 * 1/2 * 1/2 * 1/2 * 1/2 = 1/48
    # 2. サイコロの出た目が2のとき
    # 1/6 * 2/2 * 1/2 * 1/2 * 1/2 * 1/2 = 1/24
    # 3. サイコロの出た目が3のとき
    # 1/6 * 4/2 * 1/2 * 1/2 * 1/2 * 1/2 = 1/12
    # 4. サイコロの出た目が4のとき
    # 1/6 * 8/2 * 1/2 * 1/2 * 1/2 * 1/2 = 1/6
    # 5. サイコロの出た目が5のとき
    # 1/6 * 16/2 * 1/2 * 1/2 * 1/2 * 1/2 = 1/3
    # 6. サイコロの出た目が6のとき
    # 1/6 * 32/2 * 1/2 * 1/2 * 1
