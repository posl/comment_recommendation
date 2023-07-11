Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(input())
    for i in range(n):
        for j in range(n):
            if i != j:
                if a[i][j] == 'W' and a[j][i] != 'L':
                    print('incorrect')

=======
Suggestion 2

def judge(A):
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] == "W":
                if A[j][i] != "L":
                    return False
            elif A[i][j] == "L":
                if A[j][i] != "W":
                    return

=======
Suggestion 3

def main():
    n = int(input())
    a = [input() for i in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] == "W" and a[j][i] != "L":
                print("incorrect")
                return
            elif a[i][j] == "L" and a[j][

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i][j] == 'W' and a[j][i] != 'L':
                print('inco

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == 'W' and A[j][i] != 'L':
                print('inco

=======
Suggestion 6

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'W':
                if a[j][i] != 'L':
                    print("incorrect")

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    for i in range(n):
        for j in range(n):
            if i != j:
                if a[i][j] == "W" and a[j][i] != "L":
                    print("incorrect")

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    for i in range(N):
        for j in range(N):
            if A[i][j] != A[j][i]:
                print("incorrect")
                return
    print("correct")
    return

=======
Suggestion 9

def problem261_b():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())

    for i in range(N):
        for j in range(N):
            if i != j:
                if A[i][j] == 'W' and A[j][i] != 'L':
                    print("incorrect")

=======
Suggestion 10

def check(a, n):
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'W':
                if a[j][i] != 'L':
                    return False
            elif a[i][j] == 'L':
                if a[j][i] != 'W':
                    return False
