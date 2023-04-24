Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    S = sum(A)
    for x in X:
        print(S - N * x)

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - i
    B.sort()
    B = [0] + B
    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = S[i - 1] + B[i]
    for x in X:
        ok = 0
        ng = N
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if B[mid] <= x:
                ok = mid
            else:
                ng = mid
        ans = (x + 1) * ok - S[ok]
        ans += S[N] - S[ok] - (x + 1) * (N - ok)
        print(ans)

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    #print(n, q, a, x)
    #a.sort()
    #print(a)
    #print(x)
    #print()
    for i in range(q):
        #print("x[i]={}".format(x[i]))
        #print("a={}".format(a))
        #print("x[i]={}".format(x[i]))
        #print("a={}".format(a))
        #print("a[0]={}".format(a[0]))
        #print("a[n-1]={}".format(a[n-1]))
        #print("a[n]={}".format(a[n]))
        #print()
        if x[i] < a[0]:
            print(a[0]-x[i])
        elif x[i] > a[n-1]:
            print(x[i]-a[n-1])
        else:
            #print("a={}".format(a))
            #print("x[i]={}".format(x[i]))
            #print("a[0]={}".format(a[0]))
            #print("a[n-1]={}".format(a[n-1]))
            #print("a[n]={}".format(a[n]))
            #print()
            j = 0
            k = n
            while k-j > 1:
                #print("j={}, k={}".format(j, k))
                m = (j+k)//2
                #print("m={}".format(m))
                if a[m] == x[i]:
                    #print("a[m] == x[i]")
                    print(0)
                    break
                elif a[m] < x[i]:
                    #print("a[m] < x[i]")
                    j = m
                else:
                    #print("a[m] > x[i]")
                    k = m
            else:
                #print("j={}, k={}".format(j, k))
                #print("a[j]={}, a[k]={}".format(a[j], a[k]))
                #print("x[i]={}".format(x[i]))
                print(min(x[i]-a[j], a[k]-x[i]))

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]

    for x in X:
        print(sum(abs(a-x) for a in A))

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]

    # Aの要素を全てXにするのに必要な最小の操作回数を求める
    # 操作は2通りある
    # A_iから1を減算する
    # A_iに1を加算する
    # どちらを選んでも結果は変わらないので、A_iとXの差が奇数なら1回、偶数なら0回の操作をする
    # 0回の操作は必要ないので、全てのA_iとXの差が奇数の場合のみ考える
    # また、A_iとXの差は最大でも10^9なので、差が奇数の個数は10^9以下
    # そのため、差が奇数の個数を求める
    # この個数を全てのA_iに対して足し合わせると、最小の操作回数が求まる

    # まず、差が奇数の個数を求める
    odd_count = 0
    for a, x in zip(A, X):
        if (a - x) % 2 == 1:
            odd_count += 1

    # その個数を全てのA_iに対して足し合わせる
    for a in A:
        print(odd_count)

=======
Suggestion 7

def main():
    #入力
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    X = [int(input()) for _ in range(Q)]
    #print(N,Q,A,X)
    
    #Aの要素を全てXにする時、必要な「操作」の最小回数を求める
    #A_i に 1 を加算する。
    #A_i から 1 を減算する。
    #A_i を 2 で割る。
    #A_i に 2 を乗算する。
    #A_i に 1 を加算する。
    #A_i から 1 を減算する。
    #A_i を 2 で割る。
    #A_i に 2 を乗算する。
    #A_i に 1 を加算する。
    #A_i から 1 を減算する。
    #A_i を 2 で割る。
    #A_i に 2 を乗算する。
    #A_i に 1 を加算する。
    #A_i から 1 を減算する。
    #A_i を 2 で割る。
    #A_i に 2 を乗算する。
    #A_i に 1 を加算する。
    #A_i から 1 を減算する。
    #A_i を 2 で割る。
    #A_i に 2 を乗算する。
    #A_i に 1 を加算する。
    #A_i から 1 を減算する。
    #A_i を 2 で割る。
    #A_i に 2 を乗算する。
    #A_i に 1 を加算する。
    #A_i から 1 を減算する。
    #A_i を 2 で割る。
    #A_i に 2 を乗算する。
    #A_i に 1 を加算する。
    #A_i から 1 を減算する。
    #A_i を 2 で割る。
    #A

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    S = sum(A)
    S1 = S - N * X[0]
    S2 = S - N * X[-1]
    for i in range(1, Q):
        S1 -= X[i] - X[i-1]
        S2 -= X[Q-i-1] - X[Q-i]
        print(S1 + S2)

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    # A の要素の和を求める
    A_sum = sum(A)
    # A の要素を X にした時の操作回数を求める
    for x in X:
        print(A_sum - N * x)

=======
Suggestion 10

def main():
    n,q=map(int,input().split())
    A=list(map(int,input().split()))
    X=[int(input()) for i in range(q)]
    #print(A,X)
    for i in range(q):
        #print(X[i])
        #print(A)
        count=0
        for j in range(n):
            if X[i]==A[j]:
                continue
            elif X[i]<A[j]:
                count+=A[j]-X[i]
            else:
                count+=X[i]-A[j]
        print(count)
