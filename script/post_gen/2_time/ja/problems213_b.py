Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[1])

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[1])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[N-2])

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(a.index(sorted(a)[1]) + 1)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[n-2])

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 1. スコアが小さい順にソート
    A.sort()
    # 2. 2番目のスコアを出力
    print(A[1])
