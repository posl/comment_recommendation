Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1
    print(*B)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = [0]*N
    for i in range(N):
        ans[A[i]-1] = i+1
    print(*ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1

    print(" ".join(map(str, B)))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [-1] * N
    for i in range(N):
        B[A[i]-1] = i+1
    print(*B)

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = [0] * N
    for i in range(N):
        ans[A[i]-1] = i + 1
    print(*ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    for i in range(N):
        if A[i] == N:
            print(i + 1, end = " ")
    for i in range(N):
        if A[i] != N:
            print(i + 1, end = " ")

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 逆順に見ていく
    A.reverse()
    # 1人目の出席番号を出力する
    print(A[0])
    # 2人目以降の出席番号を出力する
    for i in range(1, N):
        print(A[i] - sum(A[:i]))
