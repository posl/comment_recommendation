Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]
    ans = 10**18
    for i in range(1, n-1):
        for j in range(i+1, n):
            ans = min(ans, max(s[i], s[j]-s[i], s[n]-s[j]) - min(s[i], s[j]-s[i], s[n]-s[j]))
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    C = [0] * N
    D = [0] * N
    E = [0] * N
    for i in range(N):
        B[i] = B[i - 1] + A[i]
        E[i] = E[i - 1] + A[N - 1 - i]
    for i in range(1, N - 2):
        C[i] = C[i - 1] + A[i]
    for i in range(2, N - 1):
        D[i] = D[i - 1] + A[N - i]
    ans = 10 ** 9
    for i in range(1, N - 2):
        ans = min(ans, max(B[i], C[i], D[N - i], E[N - i]) - min(B[i], C[i], D[N - i], E[N - i]))
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))

    #累積和
    s = [0] * (n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]

    #最小値の累積和
    min_s = [0] * (n+1)
    min_s[0] = s[0]
    for i in range(1, n+1):
        min_s[i] = min(min_s[i-1], s[i])

    #最大値の累積和
    max_s = [0] * (n+1)
    max_s[0] = s[0]
    for i in range(1, n+1):
        max_s[i] = max(max_s[i-1], s[i])

    ans = 10**9
    for i in range(3, n-1):
        ans = min(ans, max(max_s[i]-min_s[i], max_s[n]-max_s[i], max_s[i]-min_s[i], max_s[n]-max_s[i]) - min(max_s[i]-min_s[i], max_s[n]-max_s[i], max_s[i]-min_s[i], max_s[n]-max_s[i]))

    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 累積和を求める
    cumsum = [0] * (N + 1)
    for i in range(N):
        cumsum[i + 1] = cumsum[i] + A[i]

    # 最小値の更新
    mincumsum = [0] * (N + 1)
    mincumsum[0] = cumsum[0]
    for i in range(N):
        mincumsum[i + 1] = min(mincumsum[i], cumsum[i + 1])

    # 最大値の更新
    maxcumsum = [0] * (N + 1)
    maxcumsum[0] = cumsum[0]
    for i in range(N):
        maxcumsum[i + 1] = max(maxcumsum[i], cumsum[i + 1])

    # 3箇所で切る
    ans = 10 ** 18
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            # B, C, D, E
            B = cumsum[i]
            C = cumsum[j] - cumsum[i]
            D = cumsum[N] - cumsum[j]
            E = cumsum[N] - cumsum[N - 1]
            # P, Q, R, S
            P = B
            Q = C
            R = D
            S = E
            # P, Q, R, S の最大値と最小値の差の絶対値の最小値を求める
            ans = min(ans, max(P, Q, R, S) - min(P, Q, R, S))

            # B, C, D, E
            B = cumsum[i]
            C = cumsum[j] - cumsum[i]
            D = cumsum[N] - cumsum[j]
            E = cumsum[N - 1] - cumsum[j - 1]
            # P, Q, R, S
            P = B
            Q = C
            R = D
            S = E
            # P, Q, R, S の最

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A = [3, 2, 4, 1, 2]
    # N = 5
    # A = [10, 71, 84, 33, 6, 47, 23, 25, 52, 64]
    # N = 10
    # A = [1, 2, 3, 1000000000, 4, 5, 6]
    # N = 7
    # A = [10, 71, 84, 33, 6, 47, 23, 25, 52, 64]
    # N = 10
    # A = [1, 2, 3, 1000000000, 4, 5, 6]
    # N = 7

    # N = int(input())
    # A = list(map(int, input().split()))

    # 1. 1つ目の切り口を固定する
    # 2. 2つ目の切り口を固定する
    # 3. 3つ目の切り口を固定する
    # 4. 4つ目の切り口を固定する
    # 5. 1,2,3,4を繰り返す

    # 1. 1つ目の切り口を固定する
    # 2. 2つ目の切り口を固定する
    # 3. 3つ目の切り口を固定する
    # 4. 4つ目の切り口を固定する
    # 5. 1,2,3,4を繰り返す

    # 1. 1つ目の切り口を固定する
    # 2. 2つ目の切り口を固定する
    # 3. 3つ目の切り口を固定する
    # 4. 4つ目の切り口を固定する

=======
Suggestion 6

def main():
    # 入力
    N = int(input())
    A = list(map(int, input().split()))

    # 累積和
    sum_A = [0]
    for i in range(N):
        sum_A.append(sum_A[i] + A[i])

    # 3箇所で切る
    # 3箇所の位置を固定する
    ans = float("inf")
    for i in range(1, N-1):
        for j in range(i+1, N):
            # 3箇所の位置を固定して、それぞれの総和を求める
            P = sum_A[i]
            Q = sum_A[j] - sum_A[i]
            R = sum_A[N] - sum_A[j]
            # 最大値と最小値の差の絶対値を求める
            ans = min(ans, max(P, Q, R) - min(P, Q, R))

    # 出力
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 先頭から累積和をとる
    acc = [0]
    for a in A:
        acc.append(acc[-1] + a)

    # 3つめの切り口を固定する
    ans = float("inf")
    for i in range(3, N - 1):
        # 1つめの切り口を固定する
        for j in range(i - 2):
            # 2つめの切り口を固定する
            for k in range(j + 1, i - 1):
                # 総和を求める
                p = acc[k] - acc[j]
                q = acc[i] - acc[k]
                r = acc[N] - acc[i]
                s = acc[j]
                # 最大値と最小値の差の絶対値を求める
                ans = min(ans, max(p, q, r, s) - min(p, q, r, s))

    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    A = list(map(int, input().split()))
    s = sum(A)
    left = 0
    right = 0
    left_s = A[0]
    right_s = s - A[0]
    min_dif = abs(left_s - right_s)
    for i in range(n - 1):
        if left_s < right_s:
            left += 1
            left_s += A[left]
        else:
            right += 1
            right_s -= A[right]
        dif = abs(left_s - right_s)
        if dif < min_dif:
            min_dif = dif
    print(min_dif)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print(len(A))
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A[7])
    #print(A[8])
    #print(A[9])
    #print(A[10])
    #print(A[11])
    #print(A[12])
    #print(A[13])
    #print(A[14])
    #print(A[15])
    #print(A[16])
    #print(A[17])
    #print(A[18])
    #print(A[19])
    #print(A[20])
    #print(A[21])
    #print(A[22])
    #print(A[23])
    #print(A[24])
    #print(A[25])
    #print(A[26])
    #print(A[27])
    #print(A[28])
    #print(A[29])
    #print(A[30])
    #print(A[31])
    #print(A[32])
    #print(A[33])
    #print(A[34])
    #print(A[35])
    #print(A[36])
    #print(A[37])
    #print(A[38])
    #print(A[39])
    #print(A[40])
    #print(A[41])
    #print(A[42])
    #print(A[43])
    #print(A[44])
    #print(A[45])
    #print(A[46])
    #print(A[47])
    #print(A[48])
    #print(A[49])
    #print(A[50])
    #print(A[51])
    #print(A[52])
    #print(A[53])
    #print(A[54])
    #print(A[55])
    #print(A[56])
    #print(A[57])
    #print(A[58])
    #print(A[59])
    #print(A[60])
    #print(A[61])
    #print(A[62])
    #print(A[63])
    #print(A[64])
    #print(A[65])
    #print

=======
Suggestion 10

def main():
    # 入力
    n = int(input())
    a = list(map(int, input().split()))
    # 3箇所で切る
    # 1箇所目の切り方
    # 1箇所目の切り方は2通り
    # 1箇所目の切り方の1通目
    # 1
