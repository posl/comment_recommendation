Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    board = [0, 0, 0, 0]
    for i in range(N):
        board[0] += 1
        for j in range(4):
            if board[j] > 0:
                board[j] -= 1
                board[j + A[i]] += 1
        for k in range(4):
            if board[k] > 1:
                P += board[k] - 1
                board[k] = 1
    print(P)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        if a[i] == 1:
            p += 1
        elif a[i] == 2:
            p += 2
        elif a[i] == 3:
            p += 3
        elif a[i] == 4:
            p += 4
    print(p)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        if i == 0:
            P += 1
        else:
            P += A[i-1]
        if P >= 4:
            P -= 4
    print(P)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        if i == 0:
            P += 1
        else:
            P += 1
            P -= 1
    print(P)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        P += A[i] // 4
        A[i] = A[i] % 4
        if sum(A) >= 4:
            P += sum(A) // 4
            A = [a % 4 for a in A]
    print(P)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        if i == 0:
            p = 0
        else:
            p += a[i-1]
    print(p)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        if i == 0:
            p += 1
        else:
            if a[i-1] == 1:
                p += 1
            elif a[i-1] == 2:
                p += 1
            elif a[i-1] == 3:
                p += 2
            elif a[i-1] == 4:
                p += 3
    print(p)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int,input().split()))
    p = 0
    for i in range(n):
        p += 1
        p += (p + a[i]) // 4
        p -= (p + a[i]) // 4 * 4
    print(p)

=======
Suggestion 9

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    p = 0
    for i in range(n):
        p += 1
        if p == 4:
            p -= 4
    print(p)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        P += 1
        P += int((P + A[i]) / 4)
    print(P)

main()
