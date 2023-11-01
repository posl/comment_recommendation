Synthesizing 10/10 solutions

=======
Suggestion 1

def check_table(table):
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == 'W':
                if table[j][i] != 'L':
                    return False
            elif table[i][j] == 'L':
                if table[j][i] != 'W':
                    return False
            elif table[i][j] == 'D':
                if table[j][i] != 'D':
                    return False
    return True

=======
Suggestion 2

def check():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            elif A[i][j] == 'W' and A[j][i] != 'L':
                return 'incorrect'
            elif A[i][j] == 'L' and A[j][i] != 'W':
                return 'incorrect'
            elif A[i][j] == 'D' and A[j][

=======
Suggestion 3

def main():
    n = int(input())
    A = []
    for i in range(n):
        A.append(input())
    #print(A)
    for i in range(n):
        for j in range(n):
            if i == j:
                pass
            elif A[i][j] == 'W' and A[j][i] != 'L':
                print('incorrect')
                return
            elif A[i][j] == 'L' and A[j][i] != 'W':
                print('incorrect')

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    for i in range(N):
        for j in range(N):
            if i != j:
                if A[i][j] == 'W':
                    if A[j][i] != 'L':
                        print('incorrect')
                        return
                elif A[i][j] == 'L':
                    if A[j][i] != 'W':
                        print('incorrect')

=======
Suggestion 5

def check_table(table):
    for i in range(len(table)):
        for j in range(len(table)):
            if i != j:
                if table[i][j] == "W" and table[j][i] != "L":
                    return False
                elif table[i][j] == "L" and table[j][i] != "W":
                    return False
                elif table[i][j] == "D" and table[j][i] != "D":

=======
Suggestion 6

def main():
    n = int(input())
    a = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'W' and a[j][i] != 'L':
                print('incorrect')
                return
            elif a[i][j] == 'L' and a[j][i] != 'W':
                print('incorrect')
                return
            elif a[i][j] == 'D' and a[j][i] != 'D':
                pr

=======
Suggestion 7

def check_table(table):
    for i in range(len(table)):
        for j in range(len(table)):
            if i != j:
                if table[i][j] == 'W' and table[j][i] != 'L':
                    return False
                elif table[i][j] == 'L' and table[j][i] != 'W':
                    return False
                elif table[i][j] == 'D' and table[j][i] != 'D':

=======
Suggestion 8

def check(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == 'W':
                if a[j][i] != 'L':
                    return False
            elif a[i][j] == 'L':
                if a[j][i] != 'W':
                    return False
            elif a[i][j] == 'D':
                if a[j][i] != 'D':
                    return False
    return True

=======
Suggestion 9

def main():
    N = int(input())
    A = [input() for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == 'W' and A[j][i] != 'L':
                print('incorrect')
                return
            if A[i][j] == 'L' and A[j][i] != 'W':
                print('incorrect')
                return

=======
Suggestion 10

def check(a, n):
    for i in range(n):
        for j in range(n):
            if a[i][j] == "W":
                if a[j][i] != "L":
                    return "incorrect"
            elif a[i][j] == "L":
                if a[j][i] != "W":
                    return "incorrect"
            elif a[i][j] == "D":
                if a[j][i] != "D":
                    return "incorrect"
    return "correct"
