Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    ans = float('inf')
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            ans = min(ans, max(S[i], S[j] - S[i], S[N] - S[j]) - min(S[i], S[j] - S[i], S[N] - S[j]))
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0] * (N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    ans = 10**9
    for i in range(1, N-1):
        for j in range(i+1, N):
            ans = min(ans, max(S[i], S[j]-S[i], S[-1]-S[j]) - min(S[i], S[j]-S[i], S[-1]-S[j]))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 累積和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]

    # 部分列の和の最大値と最小値の差の絶対値を求める
    def calc(s, e):
        # 累積和の差
        diff = S[e] - S[s]
        # 部分列の和の最大値と最小値の差の絶対値
        return max(diff, S[-1] - diff)

    # 3箇所で切る
    ans = 10 ** 9
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            # i, jを切る
            ans = min(ans, calc(0, i), calc(i, j), calc(j, N))

    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    Asum = [0]*(N+1)
    for i in range(N):
        Asum[i+1] = Asum[i] + A[i]
    #print(Asum)
    ans = 10**9
    for i in range(1,N-1):
        for j in range(i+1,N):
            #print(i,j)
            P = Asum[i]
            Q = Asum[j] - Asum[i]
            R = Asum[N] - Asum[j]
            S = Asum[N] - Asum[i]
            #print(P,Q,R,S)
            ans = min(ans,max(P,Q,R,S)-min(P,Q,R,S))
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0]
    for a in A:
        S.append(S[-1] + a)
    ans = 10**9
    for i in range(1, N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                ans = min(ans, max(S[i], S[j]-S[i], S[k]-S[j], S[N]-S[k]) - min(S[i], S[j]-S[i], S[k]-S[j], S[N]-S[k]))
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0]
    for a in A:
        S.append(S[-1] + a)
    ans = 10 ** 9
    for i in range(1, N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                P = S[i]
                Q = S[j] - S[i]
                R = S[k] - S[j]
                S_ = S[N] - S[k]
                ans = min(ans, max(P, Q, R, S_) - min(P, Q, R, S_))
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = [A[0]]
    Q = [A[0]]
    R = [A[0]]
    S = [A[0]]
    for i in range(1, N):
        P.append(P[i - 1] + A[i])
        Q.append(Q[i - 1] + A[N - 1 - i])
        R.append(R[i - 1] + A[i])
        S.append(S[i - 1] + A[N - 1 - i])
    P = P[1:]
    Q = Q[1:]
    R = R[1:]
    S = S[1:]
    Q = Q[::-1]
    S = S[::-1]
    ans = 10**18
    for i in range(3):
        for j in range(i + 1, N - 1):
            ans = min(ans, max(P[i], Q[j], R[j] - R[i], S[N - 1] - S[j]) - min(P[i], Q[j], R[j] - R[i], S[N - 1] - S[j]))
    print(ans)

=======
Suggestion 8

def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    #累積和
    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = S[i - 1] + A[i - 1]
    #総和の最大値と最小値の差の絶対値の最小値
    ans = float("inf")
    #切る位置を全探索
    for i in range(1, N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                #P,Q,R,Sの計算
                P = S[i]
                Q = S[j] - S[i]
                R = S[k] - S[j]
                S_ = S[N] - S[k]
                #総和の最大値と最小値の差の絶対値の最小値を更新
                ans = min(ans, max(P, Q, R, S_) - min(P, Q, R, S_))
    #出力
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 10**9
    # 1つ目の切り口
    for i in range(N-3):
        # 2つ目の切り口
        for j in range(i+1,N-2):
            # 3つ目の切り口
            for k in range(j+1,N-1):
                B = A[:i+1]
                C = A[i+1:j+1]
                D = A[j+1:k+1]
                E = A[k+1:]
                P = sum(B)
                Q = sum(C)
                R = sum(D)
                S = sum(E)
                ans = min(ans, max(P,Q,R,S)-min(P,Q,R,S))
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int,input().split()))

    #N=4のときは、A[0]とA[1]を分ける、A[1]とA[2]を分ける、A[2]とA[3]を分けるの3通り
    #N=5のときは、A[0]とA[1]を分ける、A[1]とA[2]を分ける、A[2]とA[3]を分ける、A[3]とA[4]を分けるの4通り
    #N=6のときは、A[0]とA[1]を分ける、A[1]とA[2]を分ける、A[2]とA[3]を分ける、A[3]とA[4]を分ける、A[4]とA[5]を分けるの5通り
    #N=7のときは、A[0]とA[1]を分ける、A[1]とA[2]を分ける、A[2]とA[3]を分ける、A[3]とA[4]を分ける、A[4]とA[5]を分ける、A[5]とA[6]を分けるの6通り
    #N=8のときは、A[0]とA[1]を分ける、A[1]とA[2]を分ける、A[2]とA[3]を分ける、A[3]とA[4]を分ける、A[4]とA[5]を分ける、A[5]とA[6]を分ける、A[6]とA[7]を分けるの7通り
    #N=9のときは、A[0]とA[1]を分ける、A[1]とA[2]を分ける、A[2]とA[3]を分ける、A[3]とA[4]を
