Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    for i in range(Q):
        X.append(int(input()))
    for i in range(Q):
        ans = 0
        for j in range(N):
            ans += abs(A[j] - X[i])
        print(ans)

=======
Suggestion 2

def main():
    # input
    N, Q = map(int, input().split())
    As = [*map(int, input().split())]
    Xs = [*map(int, input().split())]

    # compute
    ans = []
    for X in Xs:
        ans.append(sum(abs(A-X) for A in As))

    # output
    for a in ans:
        print(a)

=======
Suggestion 3

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for i in range(Q)]
    # ある数を全てXにするために必要な操作回数は、
    # その数にXを足した数の桁数を足したもの
    # 例えば、A_i = 1234, X_i = 5678のとき、
    # 1234 + 5678 = 6912
    # 6912は4桁なので、1234に5678を足すのに必要な操作回数は4
    # これをすべてのA_iについて計算すると、
    # 1234 + 5678 = 6912
    # 3141 + 5678 = 8819
    # 2718 + 5678 = 8396
    # 1414 + 5678 = 7092
    # 1618 + 5678 = 7296
    # 0 + 5678 = 5678
    # 7777 + 5678 = 13455
    # 2552 + 5678 = 8230
    # 5368 + 5678 = 11046
    # 9982 + 5678 = 15660
    # となる。
    # これを桁数を求めるための関数を作成し、
    # それぞれのA_iに対して、A_i + X_iを計算し、
    # 桁数を求める関数に入れることで、
    # そのA_iに対してX_iを足すのに必要な操作回数を求めることができる。
    # この操作をすべてのA_iに対して行うと、
    # 6912 + 8819 + 8396 + 7092 + 7296 + 5678 + 13455 +

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - i
    B.sort()
    B_cumsum = [0] * (N + 1)
    for i in range(N):
        B_cumsum[i + 1] = B_cumsum[i] + B[i]
    for x in X:
        ok = N
        ng = -1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if B[mid] <= x:
                ok = mid
            else:
                ng = mid
        print(N * x + B_cumsum[ok] - B_cumsum[0] - ok * (ok - 1) // 2)

=======
Suggestion 5

def main():
    import sys
    from itertools import accumulate
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    a = [0] + A
    acc = list(accumulate(a))
    for x in X:
        if x >= acc[-1]:
            print(N * x - acc[-1])
            continue
        l, r = 0, N
        while r - l > 1:
            m = (l + r) // 2
            if acc[m] <= x:
                l = m
            else:
                r = m
        print((N - l) * x - (acc[-1] - acc[l]))

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        ans = 0
        if x < A[0]:
            ans = sum(A) - N * x
        elif x > A[-1]:
            ans = N * x - sum(A)
        else:
            l, r = 0, N
            while r - l > 1:
                m = (l + r) // 2
                if A[m] <= x:
                    l = m
                else:
                    r = m
            ans = (N - l) * (x - A[l]) + sum(A[l + 1:]) - sum(A[:l + 1]) - (l + 1) * (A[l] - x)
        print(ans)

=======
Suggestion 7

def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    X = [int(input()) for _ in range(Q)]
    D = [0 for _ in range(N+1)]
    for i in range(N):
        D[i+1] = A[i] - A[i-1]
    for x in X:
        ans = 0
        for i in range(N):
            if D[i] > 0:
                ans += min(D[i],x)
            else:
                ans += max(D[i],-x)
        print(ans)

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    
    #Aの要素の最大値と最小値を求める
    min_A = min(A)
    max_A = max(A)
    
    #Aの要素の最大値と最小値の差を求める
    diff_A = max_A - min_A
    
    #Aの要素の最大値と最小値の差が0以下の場合
    if diff_A <= 0:
        #Qの要素の数だけ繰り返す
        for i in range(Q):
            #Xの要素の値を出力する
            print(X[i])
        return
    
    #Aの要素の最大値と最小値の差が1以上の場合
    #Aの要素の最大値と最小値の差を出力する
    print(diff_A)
    
    #Aの要素の最大値と最小値の差を求める
    diff_A = max_A - min_A
    
    #Aの要素の最大値と最小値の差が1以上の場合
    if diff_A > 0:
        #Aの要素の最大値と最小値の差を求める
        diff_A = max_A - min_A
        
        #Aの要素の最大値と最小値の差を出力する
        print(diff_A)
        
        #Aの要素の最大値と最小値の差を求める
        diff_A = max_A - min_A
        
        #Aの要素の最大値と最小値の差を出力する
        print(diff_A)
        
        #Aの要素の最大値と最小値の差を求める
        diff_A = max_A - min_A
        
        #Aの要素の最大値と最小値の差を出力する

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    for i in range(Q):
        X.append(int(input()))
    # Aの要素とXの要素を比較する
    # Aの要素がXの要素より大きい場合は、Aの要素をXの要素にするためには、Aの要素からXの要素を引く必要があるので、Aの要素からXの要素を引いた値を、Xの要素として配列に格納する
    # Aの要素がXの要素より小さい場合は、Aの要素をXの要素にするためには、Aの要素にXの要素を足す必要があるので、Xの要素からAの要素を引いた値を、Xの要素として配列に格納する
    for i in range(N):
        if A[i] > X[0]:
            X[0] = A[i] - X[0]
        else:
            X[0] = X[0] - A[i]
    # Xの要素の最小値を求める
    min_X = min(X)
    # Xの要素の最小値が0の場合は、Xの要素の最小値を出力する
    if min_X == 0:
        for i in range(Q):
            print(X[i])
    # Xの要素の最小値が0以外の場合は、Xの要素の最小値がXの要素の最大公約数となる
    else:
        # Xの要素の最大公約数を求める
        for i in range(Q):
            min_X = gcd(min_X, X[i])
        # Xの要素の最大公約数が0の場合は、Xの要素の最小値を出力する
        if min_X == 0:
            for i in range(Q):
                print(X[i])
        # Xの要

=======
Suggestion 10

def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    X = [int(input()) for _ in range(Q)]
    #print(N,Q,A,X)
    #print(N,Q,A,X,sep="

")
    #print(N,Q,A,X,sep="

",end="

")
    #print(N,Q,A,X,sep="

",end="

",file=sys.stderr)
    #print(N,Q,A,X,sep="

",end="

",file=sys.stderr,flush=True)
    #print(N,Q,A,X,sep="

",end="

",file=sys.stdout)
    #print(N,Q,A,X,sep="

",end="

",file=sys.stdout,flush=True)
    #print(N,Q,A,X,file=sys.stderr)
    #print(N,Q,A,X,file=sys.stderr,flush=True)
    #print(N,Q,A,X,file=sys.stdout)
    #print(N,Q,A,X,file=sys.stdout,flush=True)
    #print(N,Q,A,X,end="

")
    #print(N,Q,A,X,end="

",file=sys.stderr)
    #print(N,Q,A,X,end="

",file=sys.stderr,flush=True)
    #print(N,Q,A,X,end="

",file=sys.stdout)
    #print(N,Q,A,X,end="

",file=sys.stdout,flush=True)
    #print(N,Q,A,X,flush=True)
    #print(N,Q,A,X,flush=True,file=sys.stderr)
    #print(N,Q,A,X,flush=True,file=sys.stdout)
    #print(N,Q,A,X,sep="

",flush=True)
    #print(N,Q,A,X,sep="

",flush=True,file=sys.stderr)
    #print(N,Q,A,X,sep="

",flush=True,file=sys.stdout)
    #print(N,Q,A,X,end="

",flush=True)
    #print(N,Q,A,X,end="

",flush=True,file=sys.stderr)
    #print(N,Q,A,X,end="

",flush=True,file=sys.stdout)
    #print(N,Q,A,X,sep="

",end="

",flush=True)
    #print(N,Q,A,X,sep="

",end="

",flush=True,file=sys.stderr)
    #print(N,Q,A,X,sep="

",end="

",flush=True,file=sys.stdout)
