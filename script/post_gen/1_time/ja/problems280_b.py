Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0] * N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - A[i-1]
    print(*A)

main()

=======
Suggestion 2

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0] * N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - A[i-1]
    print(*A)

=======
Suggestion 3

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0] * N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - A[i-1]
    print(' '.join(map(str, A)))

=======
Suggestion 4

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0] * N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - A[i-1]
    print(" ".join(map(str, A)))

=======
Suggestion 5

def main():
    N = int(input())
    S = list(map(int,input().split()))
    A = [0]*N
    A[0] = S[0]
    for i in range(1,N):
        A[i] = S[i]-S[i-1]
    for i in range(N):
        print(A[i],end=" ")
    print()

=======
Suggestion 6

def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = [0] * n
    a[0] = s[0]
    for i in range(1, n):
        a[i] = s[i] - s[i - 1]
    print(' '.join(map(str, a)))

=======
Suggestion 7

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0 for i in range(N)]
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - A[i-1]
    print(*A)

=======
Suggestion 8

def main():
    n = int(input())
    s = list(map(int,input().split()))
    a = []
    a.append(s[0])
    for i in range(1,n):
        a.append(s[i]-a[i-1])
    for i in range(n):
        print(a[i],end=' ')
    print()

=======
Suggestion 9

def main():
    N = int(input())
    S = [int(i) for i in input().split()]
    A = [0] * N
    for i in range(N):
        A[i] = S[i] - sum(A)
    print(' '.join(str(i) for i in A))

=======
Suggestion 10

def main():
    #入力
    N = int(input())
    S = list(map(int, input().split()))
    #Aの初期値
    A = [0 for i in range(N)]
    #Aの最初の要素を決める
    A[0] = S[0]
    #Aの残りの要素を決める
    for i in range(1, N):
        A[i] = S[i] - A[i-1]
    #出力
    print(*A)
