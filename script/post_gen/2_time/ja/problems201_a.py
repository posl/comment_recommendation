Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A = list(map(int, input().split()))
    A.sort()
    if A[2] - A[1] == A[1] - A[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    A = list(map(int, input().split()))
    A.sort()
    if A[2] - A[1] == A[1] - A[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    #入力
    A = [int(i) for i in input().split()]
    #並び替え
    A.sort()
    #出力
    if A[2]-A[1] == A[1]-A[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    #数列の長さ
    N = 3
    #数列を格納する配列
    A = [0]*N
    #数列の要素を格納
    for i in range(N):
        A[i] = int(input())
    #等差数列にできるか判定
    if (A[1]-A[0]) == (A[2]-A[1]):
        print("Yes")
    else:
        print("No")
