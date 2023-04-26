Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A = list(map(int, input().split()))
    print(min(abs(A[1] - A[0]) + abs(A[2] - A[1]), abs(A[2] - A[0]) + abs(A[1] - A[2]), abs(A[1] - A[0]) + abs(A[0] - A[2])))

=======
Suggestion 2

def main():
    a = list(map(int, input().split()))
    a.sort()
    print(a[1] - a[0] + a[2] - a[1])

=======
Suggestion 3

def main():
    A = list(map(int,input().split()))
    A.sort()
    print(A[1] - A[0] + A[2] - A[1])

=======
Suggestion 4

def main():
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, len(A)):
        ans += abs(A[i] - A[i-1])
    print(ans)

=======
Suggestion 5

def main():
    A = list(map(int, input().split()))
    A.sort()
    print(A[1] - A[0])

=======
Suggestion 6

def main():
    # 入力
    A = list(map(int, input().split()))
    # 処理
    A.sort()
    ans = A[1] - A[0]
    # 出力
    print(ans)

=======
Suggestion 7

def main():
    A = list(map(int, input().split()))
    A.sort()
    print(A[2]-A[0])

=======
Suggestion 8

def main():
    # 入力
    A = list(map(int, input().split()))
    # 出力
    print(min(A[2]-A[0], A[1]-A[0], A[1]-A[2]))
