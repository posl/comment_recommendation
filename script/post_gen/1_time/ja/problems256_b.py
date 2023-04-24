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
                if j + A[i] >= 4:
                    P += board[j]
                    board[j] = 0
                else:
                    board[j + A[i]] += board[j]
                    board[j] = 0
    print(P)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    list = [0, 0, 0, 0]
    for i in range(N):
        list[0] += 1
        for j in range(4):
            if list[j] >= A[i]:
                list[j] -= A[i]
                list[j+1] += 1
            else:
                P += list[j]
                list[j] = 0
    print(P)

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
            P += 1
            P -= (A[i-1] + A[i]) // 4
    print(P)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    P = 0
    for i in range(N):
        if i == 0:
            P += 1
        else:
            P += 1
            if i + A[i] >= 4:
                P -= 1
    print(P)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int,input().split()))
    P = 0
    for i in range(N):
        P += 1
        P -= A[i]//4
    print(P)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(len(A)):
        if i == 0:
            P += 1
        else:
            P += A[i-1]
        if P >= 4:
            P -= 4
    print(P)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        P += 1
        if P > 3:
            P -= 1
    print(P)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        P += 1
        P += (P - 1) // 4
    print(P)

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    P = 0
    for i in range(N):
        P += 1
        P += (i + A[i]) // 4
    print(P)

=======
Suggestion 10

def main():
    #input
    N = int(input())
    A = list(map(int, input().split()))

    #compute
    P = 0
    M = [0, 0, 0, 0]
    for i in range(N):
        M[0] += 1
        for j in range(4):
            if M[j] != 0:
                M[j] -= 1
                M[(j + A[i]) % 4] += 1

    for i in range(4):
        P += M[i] % 4

    #output
    print(P)
