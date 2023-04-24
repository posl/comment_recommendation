Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * n
    for i in a:
        c[i-1] += 1
    s = sum(c)
    for i in a:
        print((s-c[i-1])*(c[i-1]-1)//2)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0 for _ in range(N+1)]
    for a in A:
        B[a] += 1
    ans = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        ans[i] = (B[i] * (B[i] - 1)) // 2
    total = sum(ans)
    for a in A:
        print(total - ans[a] + (B[a] - 1) * (B[a] - 2) // 2)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))

    #各数字の出現回数を数える
    count = [0] * N
    for i in range(N):
        count[A[i]-1] += 1

    #出現回数が2以上の数字の組み合わせの数を数える
    sum = 0
    for i in range(N):
        if count[i] >= 2:
            sum += count[i] * (count[i] - 1) // 2

    #k=1,2,...,N に対して以下の問題を解いて、答えをそれぞれ出力する
    for i in range(N):
        if count[A[i]-1] >= 2:
            print(sum - (count[A[i]-1] * (count[A[i]-1] - 1) // 2) + (count[A[i]-1] - 1) * (count[A[i]-1] - 2) // 2)
        else:
            print(0)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))

    #Aの要素の個数を数える
    A_count = [0] * (N+1)
    for i in range(N):
        A_count[A[i]] += 1

    #Aの要素の個数の累積和をとる
    A_sum = [0] * (N+1)
    for i in range(1,N+1):
        A_sum[i] = A_sum[i-1] + A_count[i]

    #Aの要素の個数の累積和を用いて、答えを求める
    for i in range(N):
        ans = A_sum[N] - A_sum[A[i]] + (A_count[A[i]] - 1)
        print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int,input().split()))
    #Aの中にある数字の数を数える
    count = [0] * (N+1)
    for i in range(N):
        count[A[i]] += 1

=======
Suggestion 6

def main():
    #標準入力
    N = int(input())
    A = list(map(int, input().split()))
    #Aの要素の個数をカウントする
    count = [0] * (N+1)
    for i in range(N):
        count[A[i]] += 1
    #countの要素の値を合計する
    total = 0
    for i in range(N+1):
        total += count[i] * (count[i] - 1) // 2
    #出力
    for i in range(N):
        print(total - (count[A[i]] - 1))

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    # A[i]の出現回数をカウント
    count = [0 for _ in range(N + 1)]
    for a in A:
        count[a] += 1
    # A[i]が1つだけの場合は0を出力
    for a in A:
        if count[a] == 1:
            print(0)
        else:
            # A[i]が複数ある場合は、N-1個のボールから2つ選ぶ組み合わせからA[i]を除いた組み合わせを引く
            print((N - 1) * (N - 2) // 2 - (count[a] - 1) * (count[a] - 2) // 2)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    #print(A)
    #print(N)
    #print(A)
    #print(A)

    # 1. Aの各要素の個数を数える
    # 2. Aの各要素の個数の組み合わせを計算する
    # 3. Aの各要素の個数の組み合わせから、Aの各要素の個数を引く
    # 4. Aの各要素の個数の組み合わせから、Aの各要素の個数を引いたものを出力する
    # 5. Aの各要素の個数を出力する

    # 1. Aの各要素の個数を数える
    # 2. Aの各要素の個数の組み合わせを計算する
    # 3. Aの各要素の個数の組み合わせから、Aの各要素の個数を引く
    # 4. Aの各要素の個数の組み合わせから、Aの各要素の個数を引いたものを出力する
    # 5. Aの各要素の個数を出力する

    # 1. Aの各要素の個数を数える
    # 2. Aの各要素の個数の組み合わせを計算する
    # 3. Aの各要素の個数の組み合わせから、Aの各要素の個数を引く
    # 4. Aの各要素の個数の組み合わせから、Aの各要素の個数を引いたものを出力する
    # 5. Aの各要素の個数を出力する

    #

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 1. Aの数字をカウント
    # 2. Aの数字のカウントの組み合わせを計算
    # 3. Aの数字のカウントの組み合わせから2を引く
    # 4. 3で0以下になったら0を出力
    # 5. 3で0より大きい数を出力
    # 1.
    A_count = [0] * (N + 1)
    for a in A:
        A_count[a] += 1
    # 2.
    A_count_combination = [0] * (N + 1)
    for a in A_count:
        A_count_combination[a] += 1
    # 3.
    A_count_combination = [a * (a - 1) // 2 for a in A_count_combination]
    # 4.
    A_count_combination = [a - 2 for a in A_count_combination]
    A_count_combination = [0 if a < 0 else a for a in A_count_combination]
    # 5.
    A_count_combination = [a * (N - 1) for a in A_count_combination]
    A_count_combination = [a // 2 for a in A_count_combination]
    for a in A_count_combination[1:]:
        print(a)
