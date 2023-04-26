Synthesizing 10/10 solutions

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
    while i < N and j < M:
        if A[i] >= B[j]:
            if A[i] == B[j]:
                i += 1
            j += 1
        else:
            i += 1
    if j == M:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    # 入力を受け取る
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 長さのリストを作成する
    a = [0] * (10**9 + 1)
    for i in range(N):
        a[A[i]] = 1
    # 食事計画を実行できるかどうかを調べる
    for i in range(M):
        if a[B[i]] == 0:
            print('No')
            return
    # 食事計画を実行できる場合
    print('Yes')

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()

    for i in range(M):
        if A[i] != B[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 4

def main():
    # 入力を受け取る
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 2つのリストをソートする
    A.sort()
    B.sort()
    # 2つのリストの要素を比較し、
    # どちらかのリストの要素がもう一方のリストの要素より小さい場合は No を出力し、
    # どちらのリストの要素ももう一方のリストの要素より大きい場合は Yes を出力する
    for i in range(M):
        if A[i] < B[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = sorted(A)
    B = sorted(B)
    for i in range(M):
        if A[i] < B[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    A.sort()
    B.sort()
    
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] < B[j]:
            i += 1
        elif A[i] == B[j]:
            i += 1
            j += 1
        else:
            print("No")
            return
    
    if j == M:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A = set(A)

    for b in B:
        if b not in A:
            print("No")
            exit()

    print("Yes")

=======
Suggestion 8

def main():
    #入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    #処理
    A.sort()
    B.sort()
    ans = "Yes"
    for b in B:
        if b not in A:
            ans = "No"
            break

    #出力
    print(ans)

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    a = a[::-1]
    b = b[::-1]
    for i in range(m):
        if a[i] < b[i]:
            print('No')
            return
    print('Yes')

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    #Aの中にBの要素があるかを調べる
    for i in range(M):
        if B[i] in A:
            A.remove(B[i])
        else:
            print("No")
            return
    print("Yes")
