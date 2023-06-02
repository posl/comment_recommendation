Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    for i in range(N):
        for j in range(N):
            if A[i][j] == 'W':
                if A[j][i] != 'L':
                    print('不正确')
                    return
            elif A[i][j] == 'L':
                if A[j][i] != 'W':
                    print('不正确')
                    return
            elif A[i][j] == 'D':
                if A[j][i] != 'D':
                    print('不正确')
                    return
    print('正确')

=======
Suggestion 2

def main():
    N = int(input())
    A = [list(input()) for i in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == 'W':
                if A[j][i] != 'L':
                    print('不正确')
                    return
            elif A[i][j] == 'L':
                if A[j][i] != 'W':
                    print('不正确')
                    return
            elif A[i][j] == 'D':
                if A[j][i] != 'D':
                    print('不正确')
                    return
    print('正确')

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    for i in range(n):
        for j in range(n):
            if i != j:
                if a[i][j] == 'W':
                    if a[j][i] == 'W':
                        print('不正确')
                        return
                    if a[j][i] == 'D':
                        print('不正确')
                        return
                if a[i][j] == 'L':
                    if a[j][i] == 'L':
                        print('不正确')
                        return
                    if a[j][i] == 'D':
                        print('不正确')
                        return
                if a[i][j] == 'D':
                    if a[j][i] == 'W':
                        print('不正确')
                        return
                    if a[j][i] == 'L':
                        print('不正确')
                        return
    print('正确')
    return

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
                if A[i][j] == "W":
                    if A[j][i] != "L":
                        print("不正确")
                        exit()
                elif A[i][j] == "L":
                    if A[j][i] != "W":
                        print("不正确")
                        exit()
                elif A[i][j] == "D":
                    if A[j][i] != "D":
                        print("不正确")
                        exit()
    print("正确")

=======
Suggestion 5

def main():
    # input
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(input()))

    # process
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i][j] == 'W':
                if a[j][i] != 'L':
                    print("不正确")
                    return
            elif a[i][j] == 'L':
                if a[j][i] != 'W':
                    print("不正确")
                    return
            elif a[i][j] == 'D':
                if a[j][i] != 'D':
                    print("不正确")
                    return
    print("正确")
    return

=======
Suggestion 6

def is_correct(A):
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] == 'W':
                if A[j][i] != 'L':
                    return False
            elif A[i][j] == 'L':
                if A[j][i] != 'W':
                    return False
            elif A[i][j] == 'D':
                if A[j][i] != 'D':
                    return False
    return True

N = int(input())
A = [list(input()) for i in range(N)]
print('正确' if is_correct(A) else '不正确')

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    for i in range(N):
        for j in range(N):
            if A[i][j] == 'W':
                if A[j][i] == 'W' or A[j][i] == 'D':
                    print('不正确')
                    return
            elif A[i][j] == 'L':
                if A[j][i] == 'L' or A[j][i] == 'D':
                    print('不正确')
                    return
            elif A[i][j] == 'D':
                if A[j][i] == 'W' or A[j][i] == 'L':
                    print('不正确')
                    return
    print('正确')

=======
Suggestion 8

def main():
    n = int(input())
    result = [input() for i in range(n)]
    for i in range(n):
        for j in range(n):
            if result[i][j] == 'W':
                if result[j][i] != 'L':
                    print('不正确')
                    return
            elif result[i][j] == 'L':
                if result[j][i] != 'W':
                    print('不正确')
                    return
            elif result[i][j] == 'D':
                if result[j][i] != 'D':
                    print('不正确')
                    return
    print('正确')
    return

=======
Suggestion 9

def solve():
    #read input
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    #check
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == 'W' and A[j][i] != 'L':
                return '不正确'
            if A[i][j] == 'L' and A[j][i] != 'W':
                return '不正确'
            if A[i][j] == 'D' and A[j][i] != 'D':
                return '不正确'
    return '正确'

=======
Suggestion 10

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
