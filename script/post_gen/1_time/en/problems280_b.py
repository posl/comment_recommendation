Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0] * N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - S[i-1]
    print(*A)

main()

=======
Suggestion 2

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [S[0]]
    for i in range(1, N):
        A.append(S[i] - S[i-1])
    print(' '.join(map(str, A)))

=======
Suggestion 3

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0] * N
    for i in range(N):
        A[i] = S[i] - sum(A[:i])
    print(' '.join(map(str,A)))

=======
Suggestion 4

def main():
    n = int(input())
    s = list(map(int, input().split()))

    a = [0] * n
    a[0] = s[0]
    for i in range(1, n):
        a[i] = s[i] - s[i - 1]

    print(*a)

=======
Suggestion 5

def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = [0] * n
    for i in range(n):
        a[i] = s[i] - sum(a[:i])
    print(*a)

=======
Suggestion 6

def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = []
    for i in range(n):
        if i == 0:
            a.append(s[i])
        else:
            a.append(s[i] - sum(a))
    print(*a)

=======
Suggestion 7

def main():
    N = int(input())
    S = list(map(int,input().split()))
    A = []
    for i in range(N):
        if i == 0:
            A.append(S[i])
        else:
            A.append(S[i]-sum(A))
    print(" ".join(map(str,A)))
main()

=======
Suggestion 8

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = []
    for i in range(N):
        A.append(S[i] - sum(A))
    print(*A)

=======
Suggestion 9

def main():
    N = int(input())
    S = list(map(int,input().split()))
    A = []
    for i in range(N):
        A.append(S[i] - sum(A))
    print(*A)

main()
