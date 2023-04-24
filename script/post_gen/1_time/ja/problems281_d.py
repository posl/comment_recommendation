Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for i in range(N):
        for j in range(i+1, N):
            S.add(A[i] + A[j])
    ans = -1
    for i in S:
        if i % D == 0:
            ans = max(ans, i)
    print(ans)

=======
Suggestion 2

def main():
    N,K,D = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    S = set()
    for i in range(K):
        for j in range(i+1,K):
            S.add(A[i]+A[j])
    ans = -1
    for x in S:
        if x%D==0:
            ans = max(ans,x)
    print(ans)

=======
Suggestion 3

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, D)
    #print(A)
    S = []
    for i in range(N):
        for j in range(i+1, N):
            S.append(A[i]+A[j])
    print(S)

=======
Suggestion 4

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = A[::-1]
    if K == 1:
        print(A[0] % D)
        return
    if N == K:
        print(A[-1] % D)
        return
    B = []
    for i in range(N-1):
        B.append(A[i] - A[i+1])
    B.sort()
    B = B[::-1]
    print((A[0] - sum(B[:K-1])) % D)

=======
Suggestion 5

def main():
    #入力
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))

    #処理
    #Aの要素をDで割った余りを取り出す
    A = [a%D for a in A]

    #Aの要素をDで割った余りを集計する
    #Aの要素の最大値は100なので、100を超える余りはない
    #余りの数は100個なので、余りの数を100個の要素に持つリストを作成
    #余りが0の場合は、0の要素に1を加算
    #余りが1の場合は、1の要素に1を加算
    #余りが2の場合は、2の要素に1を加算
    #余りが3の場合は、3の要素に1を加算
    #...
    #余りが99の場合は、99の要素に1を加算
    #余りが100の場合は、0の要素に1を加算
    #余りが101の場合は、1の要素に1を加算
    #余りが102の場合は、2の要素に1を加算
    #...
    #余りが199の場合は、99の要素に1を加算
    #余りが200の場合は、0の要素に1を加算
    #余りが201の場合は、1の要素に1を加算
    #余りが202の場合は、2の要素に1を加算
    #...
    #余りが299の場合は、99の要素に1を加算
    #余りが300の場合は、0の要素に1を加算
    #...
    #余りが399の場合は、99の要素に1を加算
    #余りが400の場合は、0の要素に1を加算

=======
Suggestion 6

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    #print(A)
    #print(A[0:K])
    print(sum(A[0:K])//D)

=======
Suggestion 7

def main():
    N,K,D = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    A.sort()
    A = A[::-1]
    #print(A)
    S = set()
    for i in range(K):
        for j in range(i+1,K):
            S.add(A[i]+A[j])
    #print(S)
    if(len(S)==0):
        print(-1)
    else:
        S = list(S)
        S.sort()
        S = S[::-1]
        for i in S:
            if(i%D==0):
                print(i)
                break
        else:
            print(-1)

=======
Suggestion 8

def main():
    N,K,D = map(int,input().split())
    A = list(map(int,input().split()))

    A.sort(reverse=True)
    A = A[:K]
    #print(A)

    if D == 1:
        ans = A[-1]
    else:
        ans = -1
        for i in range(1,D):
            for j in range(len(A)):
                if A[j] % D == i:
                    ans = max(ans,A[j])
                    break
    print(ans)

=======
Suggestion 9

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()

    #A[i]を含む部分列の個数
    C = [0] * N
    #A[i]を含む部分列の個数の累積和
    S = [0] * N
    #A[i]を含む部分列の個数の累積和の最大値
    M = [0] * N

    for i in range(N):
        if i == 0:
            C[i] = 1
            S[i] = 1
            M[i] = 1
        else:
            if A[i] == A[i-1]:
                C[i] = C[i-1]
                S[i] = S[i-1] + C[i]
                M[i] = max(M[i-1], S[i])
            else:
                C[i] = 1
                S[i] = S[i-1] + C[i]
                M[i] = max(M[i-1], S[i])

    #print(A)
    #print(C)
    #print(S)
    #print(M)

    #A[i]を含む部分列の個数の累積和の最大値がK以上の場合、A[i]を含む部分列の個数はK以上
    #A[i]を含む部分列の個数の累積和の最大値がK未満の場合、A[i]を含む部分列の個数はK未満
    #A[i]を含む部分列の個数の累積和の最大値がK以上の場合、A[i]を含む部分列の個数はK以上
    #A[i]を含む部分列の個数の累積和の最大値がK未満の場合、A[i]を含む部分列の個数はK未満
    #A[i]

=======
Suggestion 10

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    
    # 配列Aの中で、A[i]を最小値として、A[i] + A[i+1] + ... + A[j] <= K*Dを満たす最大のjを求める
    # このとき、A[i] + A[i+1] + ... + A[j]は、A[i]を最小値とするK個の数の和になる
    # このK個の数をA[i]からA[j]までの数とすると、A[i] + A[i+1] + ... + A[j]は、A[i]を最小値とするK個の数の和になる
    # このK個の数をA[i]からA[j]までの数とすると、A[i] + A[i+1] + ... + A[j]は、A[i]を最小値とするK個の数の和になる
    # このK個の数をA[i]からA[j]までの数とすると、A[i] + A[i+1] + ... + A[j]は、A[i]を最小値とするK個の数の和になる
    # このK個の数をA[i]からA[j]までの数とすると、A[i] + A[i+1] + ... + A[j]は、A[i]を最小値とするK個の数の和になる
    # このK個の数をA[i]からA[j]までの数とすると、A[i] + A[i+1] + ... + A[j]は、A[i]を最小値とするK個の数の和になる
    # このK個の数をA[i]からA[j]までの数とすると、A[i] + A[i+1] + ... + A[j]は、A[i]を最小値とするK個
