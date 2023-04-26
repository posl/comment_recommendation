Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    #print(N, Q, A, X)
    #print(N, Q)
    #print(A)
    #print(X)

    # A の要素を全て X にする時、必要な「操作」の最小回数を求める
    # 0 回以上何度でも使って A の要素を全て X にする時、必要な「操作」の最小回数を求める
    # 0 回以上何度でも使って A の要素を全て X にする時、必要な「操作」の最小回数を求める
    # 0 回以上何度でも使って A の要素を全て X にする時、必要な「操作」の最小回数を求める
    # 0 回以上何度でも使って A の要素を全て X にする時、必要な「操作」の最小回数を求める
    # 0 回以上何度でも使って A の要素を全て X にする時、必要な「操作」の最小回数を求める
    # 0 回以上何度でも使って A の要素を全て X にする時、必要な「操作」の最小回数を求める
    # 0 回以上何度でも使って A の要素を全て X にする時、必要な「操作」の最小回数を求める
    # 0 回以上何度でも使って A の要素を全て X にする時、必要な「操作」の最小回数を求める
    # 0 回以上何度でも使って A の要素を全て X にする時、必要な「操作」の最小回数を求める
    # 0 回以上何度でも使って A の要素を全て X にする時、必要な「操作」の最小

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    for x in X:
        print(sum(abs(a - x) for a in A))

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    ans = [0] * Q
    for i in range(N):
        for j in range(Q):
            ans[j] += abs(A[i] - X[j])
    print('

'.join(map(str, ans)))

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]

    # 累積和をとる
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]

    # 各 X について、
    # (1) X 以下の要素の和を S から取り出す
    # (2) X 以上の要素の和を S から取り出す
    # (3) 1 と 2 の差
    # を計算し、それをすべて足したものが答え
    for x in X:
        ans = 0
        for i in range(N + 1):
            ans += min(S[i], x) * i - S[i]
        print(ans)

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]

    # 0 から 10^9 までの数値の出現回数を数える
    count = [0] * (10**9 + 1)
    for a in A:
        count[a] += 1

    # 0 から 10^9 までの数値の、それまでの数値の出現回数の累積和を求める
    cumsum = [0] * (10**9 + 1)
    for i in range(1, 10**9 + 1):
        cumsum[i] = cumsum[i-1] + count[i-1]

    # 0 から 10^9 までの数値の、それまでの数値の出現回数の累積和を求める
    cumsum2 = [0] * (10**9 + 1)
    for i in range(1, 10**9 + 1):
        cumsum2[i] = cumsum2[i-1] + cumsum[i]

    for x in X:
        # 0 から x までの数値の出現回数の累積和を求める
        cumsum3 = [0] * (x + 1)
        for i in range(1, x + 1):
            cumsum3[i] = cumsum3[i-1] + count[i]

        # 0 から x までの数値の、それまでの数値の出現回数の累積和を求める
        cumsum4 = [0] * (x + 1)
        for i in range(1, x + 1):
            cumsum4[i] = cumsum4[i-1] + cumsum3[i]

        # 0 から x までの数値の、それまでの数値の出現回数の累積和を求める
        cumsum5 = [

=======
Suggestion 6

def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    X = [int(input()) for _ in range(Q)]
    D = [0] * (N + 1)
    for i in range(N):
        D[i + 1] = D[i] + A[i]
    #print(D)
    for x in X:
        ans = 0
        for i in range(N):
            ans += min(D[i + 1] - D[i],x - D[i])
        print(ans)

main()

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]

    # A_i の値を X_i にするために必要な操作の最小回数を求める
    # A_i から X_i までの距離を d とすると
    # d が偶数のときは d // 2 回の操作で A_i を X_i にできる
    # d が奇数のときは (d + 1) // 2 回の操作で A_i を X_i にできる
    # d は A_i と X_i の偶奇が異なるときに 1 大きくなる
    # 偶奇が同じときは 0 になる
    # d は A_i と X_i の偶奇が異なるときに A_i と X_i の差の半分になる
    # 偶奇が同じときは A_i と X_i の差になる
    # d は A_i と X_i の偶奇が異なるときに A_i と X_i の差の半分になる
    # 偶奇が同じときは A_i と X_i の差になる
    # A_i と X_i の偶奇が異なるときに A_i と X_i の差の半分になる
    # 偶奇が同じときは A_i と X_i の差になる
    # A_i と X_i の偶奇が異なるときに A_i と X_i の差の半分になる
    # 偶奇が

=======
Suggestion 8

def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    A.append(10**10)
    ans = []
    for x in X:
        cnt = 0
        left = 0
        right = N
        while left < right:
            mid = (left+right) // 2
            if A[mid] <= x:
                left = mid + 1
            else:
                right = mid
        cnt += (N-left)*x
        for i in range(left):
            cnt += x-A[i]
        ans.append(cnt)
    for i in ans:
        print(i)

=======
Suggestion 9

def main():
    N,Q=map(int,input().split())
    A=list(map(int,input().split()))
    X=[int(input()) for _ in range(Q)]
    S=sum(A)
    Ss=[0 for _ in range(N+1)]
    for i in range(N):
        Ss[i+1]=Ss[i]+A[i]
    for x in X:
        if x>S:
            print(N*(x-S)+sum([i*(Ss[i]-Ss[i-1]) for i in range(1,N+1)]))
        else:
            l,r=0,N
            while l+1<r:
                m=(l+r)//2
                if Ss[m]<=x*m:
                    l=m
                else:
                    r=m
            print(sum([i*(Ss[i]-Ss[i-1]) for i in range(1,l+1)])+(l+1)*(x*l-Ss[l]))
