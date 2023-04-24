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
            if board[j] >= 1:
                if j + A[i] < 4:
                    board[j + A[i]] += 1
                    board[j] -= 1
                else:
                    P += board[j]
                    board[j] -= board[j]
    print(P)

=======
Suggestion 2

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    p = 0
    s = [0, 0, 0, 0]
    for i in range(n):
        s[0] += 1
        for j in range(4):
            if s[j] > 0:
                if j + a[i] >= 4:
                    p += s[j]
                    s[j] = 0
                else:
                    s[j + a[i]] += s[j]
                    s[j] = 0
    print(p)

=======
Suggestion 3

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
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        if A[i] == 1:
            P += 1
        elif A[i] == 2:
            P += 2
        elif A[i] == 3:
            P += 3
        elif A[i] == 4:
            P += 4
    print(P)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        if i == 0:
            P = 0
        else:
            P = P + A[i-1] - 1
    print(P)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        if i == 0:
            P = 0
        else:
            P = P + A[i-1]
        if P >= 4:
            P = P - 4
        if P == 0:
            if A[i] == 1:
                P = P + 1
            elif A[i] == 2:
                P = P + 2
            elif A[i] == 3:
                P = P + 3
            elif A[i] == 4:
                P = P + 4
        elif P == 1:
            if A[i] == 1:
                P = P + 1
            elif A[i] == 2:
                P = P + 2
            elif A[i] == 3:
                P = P + 3
            elif A[i] == 4:
                P = P + 4
        elif P == 2:
            if A[i] == 1:
                P = P + 1
            elif A[i] == 2:
                P = P + 2
            elif A[i] == 3:
                P = P + 3
            elif A[i] == 4:
                P = P + 4
        elif P == 3:
            if A[i] == 1:
                P = P + 1
            elif A[i] == 2:
                P = P + 2
            elif A[i] == 3:
                P = P + 3
            elif A[i] == 4:
                P = P + 4
    print(P)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        P += A[i]
        if P >= 4:
            P -= 4
    print(P)

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    P = 0
    for i in A:
        P += i//2
    print(P)

=======
Suggestion 9

def main():
    #Read input
    N = int(input())
    A = list(map(int,input().split()))
    
    #Initialize variables
    P = 0
    squares = [0,0,0,0]
    
    #Perform operations
    for i in range(N):
        squares[0] += 1
        for j in range(1,4):
            squares[j] += squares[j-1]
            squares[j-1] = 0
        squares[3] += squares[2]
        squares[2] = 0
        P += squares[3]
        squares[3] = 0
        squares[A[i]-1] += 1
    print(P)

=======
Suggestion 10

def main():
    #read input
    n = int(input())
    a = [int(x) for x in input().split()]
    #initialize variables
    p = 0
    board = [0, 0, 0, 0]
    #perform operations
    for i in range(n):
        board[0] += 1
        for j in range(4):
            if board[j] > 0:
                if j + a[i] < 4:
                    board[j + a[i]] += board[j]
                else:
                    p += board[j]
                board[j] = 0
    #print output
    print(p)
