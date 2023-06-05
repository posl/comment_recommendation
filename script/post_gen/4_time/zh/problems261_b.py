Synthesizing 10/10 solutions

=======
Suggestion 1

def check(n, a):
    for i in range(n):
        for j in range(n):
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
Suggestion 2

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(input()))
    for i in range(N):
        for j in range(N):
            if A[i][j] == 'W':
                if A[j][i] != 'L':
                    print('不正确')
                    exit()
            elif A[i][j] == 'L':
                if A[j][i] != 'W':
                    print('不正确')
                    exit()
            elif A[i][j] == 'D':
                if A[j][i] != 'D':
                    print('不正确')
                    exit()
    print('正确')

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    flag = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            elif a[i][j] == 'W':
                if a[j][i] != 'L':
                    flag = 1
            elif a[i][j] == 'L':
                if a[j][i] != 'W':
                    flag = 1
            elif a[i][j] == 'D':
                if a[j][i] != 'D':
                    flag = 1
    if flag == 1:
        print('不正确')
    else:
        print('正确')

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
            if A[i][j] == 'L':
                if A[j][i] != 'W':
                    print("不正确")
                    return
            if A[i][j] == 'D':
                if A[j][i] != 'D':
                    print("不正确")
                    return
    print("正确")
    return

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'W' and a[j][i] != 'L':
                print('No')
                return
            elif a[i][j] == 'L' and a[j][i] != 'W':
                print('No')
                return
            elif a[i][j] == 'D' and a[j][i] != 'D':
                print('No')
                return
    print('Yes')

=======
Suggestion 6

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(input()))
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
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    for i in range(N):
        for j in range(N):
            if i != j:
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
    return

=======
Suggestion 8

def main():
    n = int(input())
    a = [input() for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i][j] == 'W' and a[j][i] != 'L':
                print('不正确')
                return
            if a[i][j] == 'L' and a[j][i] != 'W':
                print('不正确')
                return
            if a[i][j] == 'D' and a[j][i] != 'D':
                print('不正确')
                return
    print('正确')

=======
Suggestion 9

def solve(n, a):
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'W':
                if a[j][i] != 'L':
                    return '不正确'
            elif a[i][j] == 'L':
                if a[j][i] != 'W':
                    return '不正确'
            elif a[i][j] == 'D':
                if a[j][i] != 'D':
                    return '不正确'
    return '正确'

=======
Suggestion 10

def main():
    n = int(input())
    a = [input() for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i][j] == "W" and a[j][i] != "L":
                print("不正确")
                return
            if a[i][j] == "L" and a[j][i] != "W":
                print("不正确")
                return
            if a[i][j] == "D" and a[j][i] != "D":
                print("不正确")
                return
    print("正确")
    return
