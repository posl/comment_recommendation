Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A_max = max(A)
    A_max2 = sorted(A)[-2]
    for i in range(N):
        if A[i] == A_max:
            print(A_max2)
        else:
            print(A_max)

=======
Suggestion 2

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    max_a = max(a)
    max_a2 = sorted(a)[-2]
    for i in range(n):
        if a[i] == max_a:
            print(max_a2)
        else:
            print(max_a)

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    max_a = max(a)
    max_a_index = a.index(max_a)
    a.pop(max_a_index)
    max_a2 = max(a)
    for i in range(n):
        if i == max_a_index:
            print(max_a2)
        else:
            print(max_a)

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    # 累積和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # 最大値を求める
    max_a = max(A)
    for i in range(N):
        print(S[N] - S[i] - A[i] + max_a)

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    A_max = max(A)
    A_max_index = A.index(A_max)
    A_max2 = max(A[:A_max_index]+A[A_max_index+1:])
    for i in range(N):
        if i == A_max_index:
            print(A_max2)
        else:
            print(A_max)

=======
Suggestion 6

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    # Aの最大値を求める
    max_a = max(A)

    # Aの最大値のindexを求める
    max_a_index = A.index(max_a)

    # Aの最大値を除いたリストを作る
    A.remove(max_a)

    # Aの最大値を除いたリストの最大値を求める
    max_a2 = max(A)

    # Aの最大値を除いたリストの最大値を出力する
    for i in range(N):
        if i == max_a_index:
            print(max_a2)
        else:
            print(max_a)

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(int(input()))
    ma = max(a)
    ma2 = max(a[:-1])
    for i in range(n):
        if a[i] == ma:
            print(ma2)
        else:
            print(ma)

=======
Suggestion 8

def main():
    #入力
    N = int(input())
    A = [int(input()) for i in range(N)]
    #解答
    A.sort()
    for i in range(N):
        if i == 0:
            print(A[-2])
        elif i == N-1:
            print(A[-2])
        else:
            print(A[-1])

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(input()) for i in range(N)]

    # Aの中で最大値を求める
    maxA = max(A)

    # Aの中で最大値を2つ以上持つ要素があるかどうか
    maxA_cnt = A.count(maxA)

    # Aの中で最大値を2つ以上持つ要素がある
    if maxA_cnt > 1:
        for i in range(N):
            print(maxA)
    # Aの中で最大値を2つ以上持つ要素がない
    else:
        # Aの中で最大値を持つ要素のindexを求める
        maxA_idx = A.index(maxA)
        # Aの中で最大値を持つ要素以外の最大値を求める
        maxA2 = max(A[:maxA_idx] + A[maxA_idx+1:])
        for i in range(N):
            if i == maxA_idx:
                print(maxA2)
            else:
                print(maxA)

=======
Suggestion 10

def main():
    #入力
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    #処理
    #最大値を求める
    A.sort()
    #print(A)
    max = A[-1]
    #print(max)
    #最大値の個数を求める
    cnt = 0
    for i in range(N):
        if A[i] == max:
            cnt += 1
    #print(cnt)
    #出力
    if cnt == 1:
        for i in range(N):
            if A[i] == max:
                print(max)
            else:
                print(max)
    else:
        for i in range(N):
            print(max)

main()
