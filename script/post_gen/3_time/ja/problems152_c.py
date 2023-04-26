Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    min = P[0]
    for i in range(N):
        if P[i] <= min:
            ans += 1
            min = P[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    minP = P[0]
    for i in range(N):
        if minP >= P[i]:
            ans += 1
            minP = P[i]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int, input().split()))
    cnt = 0
    min = P[0]
    for i in range(N):
        if P[i] <= min:
            cnt += 1
            min = P[i]
    print(cnt)

=======
Suggestion 4

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    min_P = P[0]
    for i in range(1, N):
        if min_P >= P[i]:
            ans += 1
        min_P = min(min_P, P[i])
    print(ans+1)

=======
Suggestion 5

def main():
    N = int(input())
    P = list(map(int, input().split()))
    min_num = P[0]
    cnt = 0
    for i in range(N):
        if min_num >= P[i]:
            cnt += 1
            min_num = P[i]
    print(cnt)

=======
Suggestion 6

def main():
    N = int(input())
    P = list(map(int, input().split()))
    #print(N)
    #print(P)
    min = P[0]
    count = 1
    for i in range(1, N):
        if P[i] <= min:
            count += 1
            min = P[i]
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    min_p = 1000001
    for i in range(N):
        if min_p >= P[i]:
            ans += 1
            min_p = P[i]
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    # ここに処理を書く
    # 1, ..., N の順列 P_1, ..., P_N が与えられます。
    # 次の条件を満たす整数 i(1 ≦ i ≦ N) の個数を数えてください。  
    # 任意の整数 j(1 ≦ j ≦ i) に対して、 P_i ≦ P_j
    # P_i = P[j] とすると、
    # 任意の整数 j(1 ≦ j ≦ i) に対して、 P_i ≦ P_j
    # という条件は、
    # 任意の整数 j(1 ≦ j ≦ i) に対して、 P_i >= P_j
    # という条件と同じになります。
    # つまり、P_i の値を順に比較していき、
    # その時点での最小値を更新していきます。
    # この時、最小値より小さいP_i の値があれば、
    # 条件を満たす整数 i としてカウントします。
    # また、最小値より大きいP_i の値があれば、
    # 最小値を更新します。
    # この時、最小値より大きいP_i の値があれば、
    # 条件を満たす整数 i としてカウントします。
    # このようにして、条件を満たす整数 i の個数を数えます。
    min_P = P[0]
    for i in range(1, N):
        if min_P > P[i]:
            ans += 1
        else:
            min_P = P[i]
    ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    P = list(map(int, input().split()))

    # 答えを格納する変数
    ans = 0

    # 解法
    # 1, ..., N の順列 P_1, ..., P_N が与えられます。
    # 次の条件を満たす整数 i(1 ≦ i ≦ N) の個数を数えてください。
    # 任意の整数 j(1 ≦ j ≦ i) に対して、 P_i ≦ P_j
    # 制約
    # 1 ≦ N ≦ 2 × 10^5
    # P_1, ..., P_N は 1, ..., N の順列である。
    # 入力はすべて整数である。
    # 入力
    # 入力は以下の形式で標準入力から与えられる。
    # N
    # P_1 ... P_N
    # 出力
    # 条件を満たす整数 i の個数を出力せよ。
    # 入力例 1
    # 5
    # 4 2 5 1 3
    # 出力例 1
    # 3
    # i=1,2,4 が条件を満たします。
    # i=3 は条件を満たしません。
    # 例えば、 j=1 とすると、 P_i > P_j となります。
    # 同様に、 i=5 も条件を満たしません。
    # したがって、条件を満たす整数 i の個数は 3 となります。
    # 入力例 2
    # 4
    # 4 3 2 1
    # 出力例 2
    # 4
    # すべての整数 i(1 ≦ i ≦ N) が条件を満たします。
    # 入
