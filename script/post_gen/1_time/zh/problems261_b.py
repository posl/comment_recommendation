Synthesizing 10/10 solutions

=======
Suggestion 1

def check(table):
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

=======
Suggestion 3

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
Suggestion 4

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(input()))
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == 'W':
                if A[j][i] != 'L':
                    print("不正确")
                    return
            elif A[i][j] == 'L':
                if A[j][i] != 'W':
                    print("不正确")
                    return
            elif A[i][j] == 'D':
                if A[j][i] != 'D':
                    print("不正确")
                    return
    print("正确")

main()

=======
Suggestion 5

def main():
    N = int(input())
    A = [input() for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                if A[i][j] == "W" and A[j][i] != "L":
                    print("不正确")
                    return
                elif A[i][j] == "L" and A[j][i] != "W":
                    print("不正确")
                    return
                elif A[i][j] == "D" and A[j][i] != "D":
                    print("不正确")
                    return
    print("正确")

=======
Suggestion 6

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    for i in range(n):
        for j in range(n):
            if i != j:
                if a[i][j] == 'W' and a[j][i] != 'L':
                    print('不正确')
                    return
                elif a[i][j] == 'L' and a[j][i] != 'W':
                    print('不正确')
                    return
                elif a[i][j] == 'D' and a[j][i] != 'D':
                    print('不正确')
                    return
    print('正确')

=======
Suggestion 7

def main():
    n = int(input())
    A = []
    for i in range(n):
        A.append(list(input()))
    for i in range(n):
        for j in range(n):
            if i != j and A[i][j] == "W":
                if A[j][i] != "L":
                    print("不正确")
                    return
            elif i != j and A[i][j] == "L":
                if A[j][i] != "W":
                    print("不正确")
                    return
            elif i != j and A[i][j] == "D":
                if A[j][i] != "D":
                    print("不正确")
                    return
    print("正确")

=======
Suggestion 8

def solve():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
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

def check(A):
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] == 'W' and A[j][i] != 'L':
                return False
            if A[i][j] == 'L' and A[j][i] != 'W':
                return False
            if A[i][j] == 'D' and A[j][i] != 'D':
                return False
    return True

=======
Suggestion 10

def main():
    n = int(input())
    A = []
    for i in range(n):
        A.append(list(input()))
    for i in range(n):
        for j in range(n):
            if A[i][j] == 'W':
                if A[j][i] != 'L':
                    print("不正确")
                    return
            elif A[i][j] == 'L':
                if A[j][i] != 'W':
                    print("不正确")
                    return
            elif A[i][j] == 'D':
                if A[j][i] != 'D':
                    print("不正确")
                    return
    print("正确")
