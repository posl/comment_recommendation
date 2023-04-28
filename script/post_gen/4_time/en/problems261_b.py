Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    for i in range(N):
        for j in range(N):
            if i != j:
                if A[i][j] == "W" and A[j][i] != "L":
                    print("incorrect")
                    return
                elif A[i][j] == "L" and A[j][i] != "W":
                    print("incorrect")
                    return
                elif A[i][j] == "D" and A[j][i] != "D":
                    print("incorrect")
                    return
    print("correct")

=======
Suggestion 2

def solve():
    N = int(input())
    A = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == 'W' and A[j][i] != 'L':
                return False
            if A[i][j] == 'L' and A[j][i] != 'W':
                return False
            if A[i][j] == 'D' and A[j][i] != 'D':
                return False
    return True

=======
Suggestion 3

def main():
    n = int(input())
    a = [input() for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i][j] == 'W' and a[j][i] != 'L':
                print('incorrect')
                return
            if a[i][j] == 'L' and a[j][i] != 'W':
                print('incorrect')
                return
            if a[i][j] == 'D' and a[j][i] != 'D':
                print('incorrect')
                return
    print('correct')

=======
Suggestion 4

def main():
    n = int(input())
    a = [list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i][j] == 'W' and a[j][i] != 'L':
                print('incorrect')
                return
            if a[i][j] == 'L' and a[j][i] != 'W':
                print('incorrect')
                return
            if a[i][j] == 'D' and a[j][i] != 'D':
                print('incorrect')
                return
    print('correct')

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    for i in range(n):
        for j in range(n):
            if i != j:
                if a[i][j] == 'W' and a[j][i] != 'L':
                    print('incorrect')
                    return
                elif a[i][j] == 'L' and a[j][i] != 'W':
                    print('incorrect')
                    return
                elif a[i][j] == 'D' and a[j][i] != 'D':
                    print('incorrect')
                    return
    print('correct')
    return

=======
Suggestion 6

def main():
    N = int(input())
    A = [input() for i in range(N)]

    for i in range(N):
        for j in range(N):
            if A[i][j] == 'W':
                if A[j][i] != 'L':
                    print('incorrect')
                    return
            elif A[i][j] == 'L':
                if A[j][i] != 'W':
                    print('incorrect')
                    return
            elif A[i][j] == 'D':
                if A[j][i] != 'D':
                    print('incorrect')
                    return
    print('correct')

=======
Suggestion 7

def main():
    N = int(input())
    A = [input() for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            if A[i][j] == 'W' and A[j][i] != 'L':
                print('incorrect')
                exit()
            elif A[i][j] == 'L' and A[j][i] != 'W':
                print('incorrect')
                exit()
            elif A[i][j] == 'D' and A[j][i] != 'D':
                print('incorrect')
                exit()
    print('correct')

=======
Suggestion 8

def check(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == "W":
                if a[j][i] != "L":
                    return False
            elif a[i][j] == "L":
                if a[j][i] != "W":
                    return False
            elif a[i][j] == "D":
                if a[j][i] != "D":
                    return False
    return True

n = int(input())
a = []
for i in range(n):
    a.append(input())

=======
Suggestion 9

def get_input():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    return N, A

=======
Suggestion 10

def check_result(result):
    for i in range(len(result)):
        for j in range(len(result)):
            if i != j:
                if result[i][j] == 'W':
                    if result[j][i] != 'L':
                        print("incorrect")
                        return
                elif result[i][j] == 'L':
                    if result[j][i] != 'W':
                        print("incorrect")
                        return
                elif result[i][j] == 'D':
                    if result[j][i] != 'D':
                        print("incorrect")
                        return
    print("correct")
