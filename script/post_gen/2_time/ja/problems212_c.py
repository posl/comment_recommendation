Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    ans = 10 ** 9 + 1
    while i < N and j < M:
        if A[i] < B[j]:
            ans = min(ans, B[j] - A[i])
            i += 1
        else:
            ans = min(ans, A[i] - B[j])
            j += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    ans = 10 ** 9
    while i < N and j < M:
        ans = min(ans, abs(A[i] - B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    a = 0
    b = 0
    ans = 10 ** 9
    while a < N and b < M:
        ans = min(ans, abs(A[a] - B[b]))
        if A[a] < B[b]:
            a += 1
        else:
            b += 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    ans = 10**9
    i = 0
    j = 0
    while i < N and j < M:
        ans = min(ans, abs(A[i] - B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1

    print(ans)

=======
Suggestion 5

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    a = 0
    b = 0
    ans = 1000000000000000000
    while a < N and b < M:
        if A[a] < B[b]:
            ans = min(ans,abs(A[a] - B[b]))
            a += 1
        else:
            ans = min(ans,abs(A[a] - B[b]))
            b += 1
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()

    ans = float('inf')

    i = 0
    j = 0
    while i < N and j < M:
        ans = min(ans, abs(A[i] - B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1

    print(ans)

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()
    i = 0
    j = 0
    ans = 10**9
    while i < N and j < M:
        ans = min(ans, abs(A[i] - B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # それぞれの数列から 1 つずつ要素を選んだときの 2 つの値の差の最小値
    # すなわち、  min_{ 1≦ i≦ N}min_{1≦ j≦ M} | A_i-B_j| を求めてください。
    # 1 ≦ N,M ≦ 2× 10^5
    # 1 ≦ A_i ≦ 10^9
    # 1 ≦ B_i ≦ 10^9
    # 入力は全て整数である。
    # 1. A_i と B_j の差の最小値を求める
    # 2. それぞれの数列から 1 つずつ要素を選んだときの 2 つの値の差の最小値
    # 3. それぞれの数列から 1 つずつ要素を選んだときの 2 つの値の差
    # 4. それぞれの数列から 1 つずつ要素を選んだときの 2 つの値
    # 5. それぞれの数列から 1 つずつ要素を選んだとき
    # 6. それぞれの数列から 1 つずつ要素を選んだ
    # 7. それぞれの数列から 1 つずつ要素を選ん
    # 8. それぞれの数列から 1 つずつ要素を選
    # 9. それぞれの数列から 1 つずつ要素を
    # 10. それぞれの数列から 1 つずつ要素

=======
Suggestion 9

def main():
    #入力
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    
    #A,Bを昇順にソートする
    A.sort()
    B.sort()
    
    #Aの要素のインデックスを0で初期化する
    a = 0
    #Bの要素のインデックスを0で初期化する
    b = 0
    #差の絶対値の最小値を10^9で初期化する
    min = 10**9
    
    #Aの要素のインデックスがN-1より小さい間繰り返す
    while a < N-1:
        #Bの要素のインデックスがM-1より小さい間繰り返す
        while b < M-1:
            #Aの要素とBの要素の差の絶対値を求める
            x = abs(A[a] - B[b])
            #差の絶対値の最小値と比較する
            if x < min:
                #差の絶対値の最小値を更新する
                min = x
            #Bの要素のインデックスを1増やす
            b += 1
        #Bの要素のインデックスを0にする
        b = 0
        #Aの要素のインデックスを1増やす
        a += 1
    #差の絶対値の最小値を出力する
    print(min)
