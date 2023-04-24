Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A = list(map(int, input().split()))
    print(min(abs(A[0] - A[1]) + abs(A[1] - A[2]), abs(A[0] - A[2]) + abs(A[1] - A[2]), abs(A[0] - A[1]) + abs(A[0] - A[2])))

=======
Suggestion 2

def main():
    A = list(map(int, input().split()))
    A.sort()
    print(A[1] - A[0] + A[2] - A[1])

=======
Suggestion 3

def main():
    A = list(map(int, input().split()))
    print(min(abs(A[0] - A[1]) + abs(A[2] - A[1]), abs(A[0] - A[2]) + abs(A[1] - A[2])))

=======
Suggestion 4

def main():
    A = list(map(int, input().split()))
    A.sort()
    print(A[2] - A[0])

=======
Suggestion 5

def main():
    a = list(map(int, input().split()))
    a.sort()
    print(a[1]-a[0] + a[2]-a[1])

=======
Suggestion 6

def main():
    # 入力
    A = list(map(int, input().split()))
    # 処理
    A.sort()
    # 出力
    print(A[1] - A[0] + A[2] - A[1])

=======
Suggestion 7

def main():
    # 入力
    A = list(map(int, input().split()))
    # 処理
    A.sort()
    # 出力
    print(A[1] - A[0])

=======
Suggestion 8

def main():
    # 入力
    A = list(map(int, input().split()))

    # 処理
    ans = 0
    if A[0] > A[1]:
        ans += A[0] - A[1]
    if A[2] > A[1]:
        ans += A[2] - A[1]

    # 出力
    print(ans)
