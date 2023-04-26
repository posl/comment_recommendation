Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] != X:
            print(A[i], end = " ")

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a for a in A if a != X]
    print(*A)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [i for i in A if i != X]
    print(*A)

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] != x:
            print(a[i], end=" ")
    print()

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = [i for i in a if i != x]
    print(*ans)

=======
Suggestion 6

def main():
    #input
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    #output
    for i in range(N):
        if A[i] != X:
            print(A[i], end = ' ')
    print()

=======
Suggestion 7

def main():
    # 入力
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    # 処理
    A = [i for i in A if i != X]

    # 出力
    print(*A)
