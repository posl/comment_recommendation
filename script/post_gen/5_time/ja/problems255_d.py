Synthesizing 10/10 solutions

=======
Suggestion 1

def calc(x, y):
    if x >= y:
        return x - y
    else:
        return y - x

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]

    for i in range(Q):
        count = 0
        for j in range(N):
            count += abs(A[j] - X[i])
        print(count)

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]

    a.sort()
    a.append(0)
    a.append(0)
    x.sort()
    x.append(0)
    x.append(0)

    ans = 0
    for i in range(q):
        ans += abs(a[i] - a[i+1]) * (i + 1)

    print(ans)

=======
Suggestion 4

def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    X = []
    for _ in range(Q):
        X.append(int(input()))

    # print(N,Q,A,X)

    # N,Q,A,X = 10,5,[1000000000, 314159265, 271828182, 141421356, 161803398, 0, 777777777, 255255255, 536870912, 998244353],[555555555,321654987,1000000000,789456123,0]

    # print(N,Q,A,X)

    A.sort()
    # print(A)
    # print(X)

    for x in X:
        # print("x",x)
        # print("A",A)
        # print("A[-1]",A[-1])
        # print("A[0]",A[0])
        if x >= A[-1]:
            # print("x >= A[-1]",x,A[-1])
            print(x - A[-1] + N)
        elif x <= A[0]:
            # print("x <= A[0]",x,A[0])
            print(A[0] - x + N)
        else:
            # print("x in A",x,A)
            # print("A[0]",A[0])
            # print("A[-1]",A[-1])
            # print("A[0] + N - A[-1]",A[0] + N - A[-1])
            print(A[0] + N - A[-1])

=======
Suggestion 5

def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    ans = 0
    for i in range(1, N):
        ans += abs(A[i] - A[i - 1])
    for i in range(Q):
        if i > 0:
            ans -= abs(A[X[i]] - A[X[i] - 1])
        if i < Q - 1:
            ans -= abs(A[X[i + 1]] - A[X[i]])
        ans += abs(A[X[i + 1] - 1] - A[X[i] - 1])
        print(ans)

=======
Suggestion 6

def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]

    # ここに、問題を解くためのコードを記述する
    # 1 ≦ i ≦ N を満たす整数 i を選択する。
    # 次に、以下の 2 つのうちどちらかを選択し、実行する。
    # A_i に 1 を加算する。
    # A_i から 1 を減算する。
    A.sort()
    A.append(0)
    X.sort()
    ans = 0
    for i in range(N):
        ans += abs(A[i] - A[i+1]) * (i+1)
    ans += A[N] * N
    # print(ans)

    for q in X:
        ans += abs(A[0] - q)
        print(ans)
    # 出力
    # print(ans)

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    for i in range(Q):
        X.append(int(input()))

    A.sort()
    A.insert(0,0)
    A.append(10**9+1)
    ans = 0
    for i in range(1, N+2):
        ans += (A[i]-A[i-1])*i
    print(ans)
    for i in range(Q):
        if X[i] >= A[-1]:
            ans += (X[i]-A[-1])*(N+1)
            A[-1] = X[i]
        else:
            for j in range(1, N+2):
                if X[i] >= A[j-1] and X[i] <= A[j]:
                    ans += (X[i]-A[j-1])*j
                    ans += (A[j]-X[i])*(N+1-j)
                    A[j] = X[i]
                    break
        print(ans)

=======
Suggestion 8

def main():
    # n: 数列の長さ
    # q: 質問の数
    n, q = map(int, input().split())
    # a: 数列
    a = list(map(int, input().split()))
    # x: 質問の数列
    x = [int(input()) for _ in range(q)]
    # count: 質問の数列の要素ごとの最小操作回数
    count = [0] * q
    # 質問の数列の要素ごとに操作回数を求める
    for i in range(q):
        # 質問の数列の要素
        xi = x[i]
        # 操作回数
        cnt = 0
        # 数列の要素ごとに操作回数を求める
        for j in range(n):
            # 数列の要素
            aj = a[j]
            # 操作回数を求める
            cnt += abs(xi - aj)
        # 質問の数列の要素ごとの最小操作回数を求める
        count[i] = cnt
    # 質問の数列の要素ごとの最小操作回数を出力する
    for i in range(q):
        print(count[i])

=======
Suggestion 9

def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    x = [int(input()) for _ in range(q)]
    #print(n,q,a,x)
    s = sum(a)
    for i in range(q):
        print(s+x[i])

=======
Suggestion 10

def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]

    # print(A)
    # print(X)

    # Aの最大値を求める
    maxA = max(A)

    # Aの最大値を2進数で表したときの桁数を求める
    maxA_bin = bin(maxA)
    maxA_bin_len = len(maxA_bin) - 2

    # print(maxA)
    # print(maxA_bin)
    # print(maxA_bin_len)

    # Aの全ての要素を2進数で表したときの桁数を求める
    A_bin = [bin(a) for a in A]
    A_bin_len = [len(a) - 2 for a in A_bin]

    # print(A_bin)
    # print(A_bin_len)

    # Aの全ての要素を2進数で表したときの桁数の最大値を求める
    maxA_bin_len = max(A_bin_len)

    # print(maxA_bin_len)

    # Aの全ての要素を2進数で表したときの桁数の最大値を求める
    maxA_bin_len = max(A_bin_len)

    # print(maxA_bin_len)

    # Aの全ての要素を2進数で表したときの桁数の最大値を求める
    maxA_bin_len = max(A_bin_len)

    # print(maxA_bin_len)

    # Aの全ての要素を2進数で表したときの桁数の最大値を求める
    maxA_bin_len = max(A_bin_len)

    # print(maxA_bin_len)

    # Aの全ての要素を2進数で表したときの桁数の最大値を求める
    maxA_bin_len = max(A_bin_len)

    # print(maxA_bin_len)

    # Aの全ての要素を2進数で表したときの桁数の最大値
