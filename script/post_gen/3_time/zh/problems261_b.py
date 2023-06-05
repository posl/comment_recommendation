Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    flag = False
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == 'W' and A[j][i] != 'L':
                flag = True
                break
            if A[i][j] == 'L' and A[j][i] != 'W':
                flag = True
                break
            if A[i][j] == 'D' and A[j][i] != 'D':
                flag = True
                break
        if flag:
            break
    if flag:
        print('不正确')
    else:
        print('正确')

=======
Suggestion 2

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    for i in range(n):
        for j in range(n):
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
Suggestion 3

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(input()))

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i][j] == 'W':
                if a[j][i] != 'L':
                    print('不正确')
                    return
            if a[i][j] == 'L':
                if a[j][i] != 'W':
                    print('不正确')
                    return
            if a[i][j] == 'D':
                if a[j][i] != 'D':
                    print('不正确')
                    return
    print('正确')

=======
Suggestion 4

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

n = int(input())
a = []
for i in range(n):
    a.append(list(input()))

=======
Suggestion 5

def main():
    n = int(input())
    a = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] == "W":
                if a[j][i] != "L":
                    print("不正确")
                    return
            elif a[i][j] == "L":
                if a[j][i] != "W":
                    print("不正确")
                    return
            elif a[i][j] == "D":
                if a[j][i] != "D":
                    print("不正确")
                    return
    print("正确")

=======
Suggestion 6

def check():
    n = int(raw_input())
    data = []
    for i in range(n):
        data.append(raw_input())

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if data[i][j] == 'W' and data[j][i] != 'L':
                return False
            if data[i][j] == 'L' and data[j][i] != 'W':
                return False
            if data[i][j] == 'D' and data[j][i] != 'D':
                return False
    return True

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    flag = True
    for i in range(N):
        for j in range(N):
            if i != j:
                if A[i][j] == 'W' and A[j][i] != 'L':
                    flag = False
                    break
                elif A[i][j] == 'L' and A[j][i] != 'W':
                    flag = False
                    break
                elif A[i][j] == 'D' and A[j][i] != 'D':
                    flag = False
                    break
    if flag:
        print('正确')
    else:
        print('不正确')

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'W':
                if a[j][i] != 'L':
                    print('不正确')
                    return
            elif a[i][j] == 'L':
                if a[j][i] != 'W':
                    print('不正确')
                    return
            elif a[i][j] == 'D':
                if a[j][i] != 'D':
                    print('不正确')
                    return
    print('正确')

=======
Suggestion 9

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(input()))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
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
