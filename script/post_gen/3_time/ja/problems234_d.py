Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    for i in range(K,N):
        if P[i] > P[i-K]:
            print(1)
        else:
            print(0)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P.sort()
    for i in range(K, N):
        print(P[i - K])

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = [0] * (N-K+1)
    ans[0] = min(P[:K])
    for i in range(K, N):
        ans[i-K+1] = max(P[i-K+1:i+1])
    print('

'.join(map(str, ans)))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    A = []
    for i in range(N-K+1):
        A.append(max(P[i:i+K]))
    A.sort()
    for i in range(N-K+1):
        print(A[i])

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    #print(N, K)
    #print(P)
    for i in range(K, N+1):
        #print(i)
        #print(P[0:i])
        #print(sorted(P[0:i]))
        print(sorted(P[0:i])[K-1])

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    #print(N, K)
    #print(P)

    P = [i-1 for i in P]
    #print(P)

    # 累積和
    S = [0]
    for i in P:
        S.append(S[-1] + i)
    #print(S)

    # おなじ数字を含む累積和
    # 例えば、[1, 2, 1, 1, 1] なら [1, 2, 3, 4, 5]
    S2 = [0]
    for i in P:
        S2.append(S2[-1] + i + 1)
    #print(S2)

    # おなじ数字を含む累積和の差分
    # 例えば、[1, 2, 1, 1, 1] なら [1, 1, 0, 0, 0]
    S3 = [0]
    for i in P:
        S3.append(S3[-1] + i + 1 - S2[-1] + S2[-i-2])
    #print(S3)

    for i in range(K, N+1):
        #print(i)
        #print(S[i] - S[i-K])
        #print(S2[i] - S2[i-K])
        #print(S3[i] - S3[i-K])
        print(S[i] - S[i-K] - S3[i] + S3[i-K])

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    #print(N, K)
    #print(P)
    #print(P[K-1:N])
    #print(sorted(P[K-1:N]))
    ans = sorted(P[K-1:N])
    for i in range(K):
        print(ans[i])

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    # print(N, K)
    # print(P)

    # 前処理
    # Pの累積和を求める
    # Pの累積和の累積和を求める
    # この累積和の累積和を求める
    # この累積和の累積和の累積和を求める
    # この累積和の累積和の累積和の累積和を求める
    # この累積和の累積和の累積和の累積和の累積和を求める
    # この累積和の累積和の累積和の累積和の累積和の累積和を求める
    # この累積和の累積和の累積和の累積和の累積和の累積和の累積和を求める
    # この累積和の累積和の累積和の累積和の累積和の累積和の累積和の累積和��

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    # Pの先頭K項の中で最大値を求める
    # Pの先頭K項の中で最大値を求める
    # Pの先頭K項の中で最大値を求める
    # ...
    # Pの先頭K項の中で最大値を求める
    # Pの先頭N項の中で最大値を求める
    # ということを繰り返す
    # このとき、Pの先頭K項の中で最大値を求めるたびに
    # Pの先頭K+1項の中で最大値を求めるたびに
    # Pの先頭K+2項の中で最大値を求めるたびに
    # ...
    # Pの先頭N項の中で最大値を求める�
