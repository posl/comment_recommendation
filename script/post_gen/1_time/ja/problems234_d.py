Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    # Pの先頭i項のうち、K番目に大きい値を求める
    # Pの先頭i項のうち、K番目に大きい値は、
    # Pの先頭i項のうち、K番目に大きい値以下の値の個数がK個以上ある
    # ということを利用する

    # Pの先頭i項のうち、K番目に大きい値以下の値の個数を求める
    # Pの先頭i項のうち、K番目に大きい値以下の値の個数は、
    # Pの先頭i項のうち、K番目に大きい値以下の値の個数がK個以上ある
    # ということを利用する

    # Pの先頭i項のうち、K番目に大きい値以下の値の個数がK個以上ある
    # ということは、Pの先頭i項のうち、K番目に大きい値より大きい値が
    # あるかどうかを判定することと同じ

    # Pの先頭i項のうち、K番目に大きい値以下の値の個数がK個以上ある
    # ということは、Pの先頭i項のうち、K番目に大きい値より大きい値が
    # あるかどうかを判定することと同じ

    # Pの先頭i項のうち、K番目に大きい値より大きい値があるかどうかを判定する
    # Pの先頭i項

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [p-1 for p in P]
    C = [0] * N
    for p in P:
        C[p] += 1
    S = 0
    for i in range(N):
        S += C[i]
        if S >= K:
            print(i+1)
            break

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    K -= 1
    for i in range(K, N):
        P.sort()
        print(P[K])
        P.pop(0)

=======
Suggestion 4

def main():
    #入力
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    #累積和
    cumsum = [0]*(N+1)
    for i in range(N):
        cumsum[i+1] = cumsum[i] + P[i]
    #出力
    for i in range(K,N+1):
        print(cumsum[i]-cumsum[i-K])

=======
Suggestion 5

def main():
    import sys

    def input():
        return sys.stdin.readline()[:-1]

    N, K = list(map(int, input().split()))
    P = list(map(int, input().split()))
    for i in range(K, N):
        print(P[i-K])
    return

main()

=======
Suggestion 6

def main():
    n,k=map(int,input().split())
    p=list(map(int,input().split()))
    c=[0]*(n+1)
    for i in range(n):
        c[p[i]]=i
    ans=[0]*n
    for i in range(n):
        ans[i]=c[i+1]
    ans.sort()
    for i in range(k):
        print(0)
    for i in range(k,n):
        print(ans[i]-ans[i-1])

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    #print(N, K)
    #print(P)
    #print(P[K-1])
    #print(P[K:N])
    #print(sorted(P[K-

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    #print(N, K, P)
    #print(P[:K])
    #print(sorted(P[:K]))
    #print(sorte

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    # P[i]はi+1番目に小さい値とする
    for i in range(N):
        P[i] -= 1
    # 累積和
    s = [0] * (N+1)
    for i in range(N):
        s[i+1] = s[i] + P[i]
    # 二分探索
    def binary_search(x):
        ok = N
        ng = -1
        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if s[mid] < x:
                ng = mid
            else:
                ok = mid
        return ok
    # 出力
    for i in range(K, N+1):
        print(binary_search(i))
