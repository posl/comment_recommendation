Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = [0] * (N + 1)
    for i in range(N):
        C[P[i]] = i
    for i in range(K, N + 1):
        print(max(P[:i]) - min(P[C[max(P[:i])]:i + 1]) + 1)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [p - 1 for p in P]
    C = [0] * N
    for i in range(N):
        C[P[i]] = i
    #print(P)
    #print(C)
    ans = []
    for i in range(K, N):
        #print(i)
        #print(C)
        #print(P)
        #print(P[i])
        #print(C[P[i]])
        #print(P[i] - C[P[i]])
        if P[i] - C[P[i]] >= K:
            ans.append(0)
        else:
            ans.append(1)
    print('

'.join(map(str, ans)))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [p - 1 for p in P]
    C = [0] * N
    for p in P:
        C[p] += 1
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + C[i]
    for i in range(K, N):
        print(S[P[i]] - S[P[i - K]])

=======
Suggestion 4

def main():
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [p-1 for p in P]
    #Pを累積和にする
    for i in range(N-1):
        P[i+1] += P[i]
    #print(P)
    #K番目に大きい値を求める
    for i in range(N-K+1):
        if i == 0:
            print(P[K-1])
        else:
            print(P[i+K-1] - P[i-1])

=======
Suggestion 5

def  main ( ) :
    N , K  =  map ( int , input ( ) . split ( ) )
    P  =  list ( map ( int , input ( ) . split ( ) ) )
    P  =  [ p - 1  for  p  in  P ]
    A  =  [ 0  for  _  in  range ( N ) ]
    for  i  in  range ( N ) :
        A [ P [ i ] ]  =  i
    #print(A)
     #A[i]:i+1が何番目か
    B  =  [ 0  for  _  in  range ( N ) ]
    B [ 0 ]  =  1
     #B[i]:i+1が何個あるか
    for  i  in  range ( N ) :
        B [ A [ i ] ]  +=  1
    #print(B)
     #B[i]:i+1が何個あるか
    C  =  [ 0  for  _  in  range ( N ) ]
    C [ 0 ]  =  1
     #C[i]:i+1が何個あるか
    for  i  in  range ( N ) :
        C [ B [ i ] ]  +=  1
    #print(C)
     #C[i]:i+1が何個あるか
    D  =  [ 0  for  _  in  range ( N ) ]
    D [ 0 ]  =  1
     #D[i]:i+1が何個あるか
    for  i  in  range ( N ) :
        D [ C [ i ] ]  +=  1
    #print(D)
     #D[i]:i+1が何個あるか
    E  =  [ 0  for  _  in  range ( N ) ]
    E [ 0 ]  =  1
     #E[i]:i+1が何個あるか
    for  i  in  range ( N ) :
        E [ D [ i ] ]  +=  1
    #print(E)
     #E[i]:i+1が

=======
Suggestion 6

def main():
    #入力
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    #K番目に大きい値を求める関数
    def kth_largest_value(P, K):
        #K番目に大きい値を求める
        P.sort()
        return P[-K]
    #K番目に大きい値を求める
    for i in range(K, N+1):
        print(kth_largest_value(P[:i], K))

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [p - 1 for p in P]
    # print(P)
    # print(N, K)
    # print(P)

    # Pの先頭K項のうち、K番目に大きい値を出力
    # 1,2,...,Nの順列P
    # 1番目に大きい値はN
    # 2番目に大きい値はN-1
    # 3番目に大きい値はN-2
    # ...
    # K番目に大きい値はN-K+1
    # K+1番目に大きい値はN-K
    # ...
    # N番目に大きい値は1
    # K番目に大きい値はN-K+1

    # Pの先頭K項のうち、K番目に大きい値を出力
    # Pの先頭K項のうち、K番目に小さい値を出力
    # 1,2,...,Nの順列P
    # 1番目に小さい値は1
    # 2番目に小さい値は2
    # 3番目に小さい値は3
    # ...
    # K番目に小さい値はK
    # K+1番目に小さい値はK+1
    # ...
    # N番目に小さい値はN
    # K番目に小さい値はK

    # Pの先頭K項のうち、K番目に大きい値を出力
    # Pの先頭K項のうち、K番目に小さい値を出力
    # Pの先頭K項のうち、K番目に大きい値はN-K+1

    # Pの先頭K項のうち、K番目に大きい値を出力
    #

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    # 1-indexedにする
    P.insert(0, 0)

    # Pの先頭K項の中でK番目に大きい値を求める
    # これは、Pの先頭K項の中でK番目に小さい値を求めることと同じ
    # なので、Pの先頭K項をソートしたときにK番目に小さい値を求める
    # これは、K番目に小さい値は、K番目に小さい値以外の値よりも小さくないといけない
    # つまり、K番目に小さい値は、K番目に小さい値以外の値の最大値よりも小さくないといけない
    # これを、K番目に小さい値以外の値の最大値を求めることで求めることができる
    # ここで、K番目に小さい値以外の値の最大値は、K番目に小さい値の1つ左の値である
    # なので、Pの先頭K項をソートしたときにK番目に小さい値の1つ左の値を求める
    # これは、K番目に小さい値の1つ左の値は、K番目に小さい値の1つ左の値以外の値よりも大きくないといけない
    # つまり、K番目に小さい値の1つ左の値は、K番目に小さい値の1つ左の値以外の値の最小値よりも大きくないといけない
    # これを、K番目に小さい値の1つ

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    # 1~Nの順列のうち、K番目に大きい値を求める
    # 1~Nの順列のうち、K番目に大きい値は、K番目に小さい値と等しい
    # 1~Nの順列のうち、K番目に小さい値は、K番目に大きい値と等しい
    # 1~Nの順列のうち、K番目に小さい値は、K番目に小さい値と等しい
    # 1~Nの順列のうち、K番目に大きい値は、K番目に大きい値と等しい

    # 1~Nの順列のうち、K番目に小さい値を求める
    # 順列のうち、K番目に小さい値は、K番目に小さい値と等しい

    # 1~Nの順列のうち、K番目に小さい値を求める
    # 順列のうち、K番目に小さい値は、K番目に小さい値と等しい
    # 1~Nの順列のうち、K番目に小さい値は、K番目に小さい値と等しい
    # 1~Nの順列のうち、K番目に小さい値は、K番目に小さい値と等しい

    # 1~Nの順列のうち、K番目に小さい値を求める
    # 順列のうち、K番目に小さい値は、K番目に小さい値と等しい
    # 1~Nの順列のうち、K番目に小さい値は、K番目に小さい値と等しい
    # 1

=======
Suggestion 10

def  main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [p - 1 for p in P]
    # P = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print(P)
    # P = [2, 6, 1, 4, 10, 5, 0, 8, 7, 9, 3]
    # print(P)
    # P = [3, 7, 2, 5, 11, 6, 1, 9, 8, 10, 4]
    # print(P)
    # P = [1, 2, 3]
    # print(P)
    # P = [0, 1, 2]
    # print(P)

    # Pの先頭K項のうち、K番目に大きい値
    # Pの先頭K項のうち、K番目に小さい値
    # Pの先頭K項のうち、K番目に大きい値
    # Pの先頭K項のうち、K番目に小さい値
    # Pの先頭K項のうち、K番目に大きい値
    # Pの先頭K項のうち、K番目に小さい値
    # Pの先頭K項のうち、K番目に大きい値
    # Pの先頭K項のうち、K番目に小さい値
    # Pの先頭K項のうち、K番目に大きい値
    # Pの先頭K項のうち、K番目に小さい値

    # Pの先頭K項のうち、K番目に大きい値
    # Pの先頭K項のうち、K番目に小さい値
    # Pの先頭K項のうち、K番目
