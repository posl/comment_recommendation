Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][i]:
                print("incorrect")
                return
    print("correct")

main()

=======
Suggestion 2

def main():
    n = int(input())
    a = [input() for _ in range(n)]

    for i in range(n):
        for j in range(n):
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
Suggestion 3

def check(N, A):
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

N = int(input())
A = [input() for i in range(N)]

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == "W":
                if A[j][i] != "L":
                    print("incorrect")
                    exit()
            elif A[i][j] == "L":
                if A[j][i] != "W":
                    print("incorrect")
                    exit()
            elif A[i][j] == "D":
                if A[j][i] != "D":
                    print("incorrect")
                    exit()
    print("correct")

=======
Suggestion 5

def main():
    n = int(input())
    a = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if a[i][j] == 'W':
                if a[j][i] == 'W' or a[j][i] == 'D':
                    continue
                else:
                    print('incorrect')
                    exit()
            elif a[i][j] == 'L':
                if a[j][i] == 'L' or a[j][i] == 'D':
                    continue
                else:
                    print('incorrect')
                    exit()
            elif a[i][j] == 'D':
                if a[j][i] == 'D':
                    continue
                else:
                    print('incorrect')
                    exit()

    print('correct')
    return

main()

=======
Suggestion 6

def main():
    n = int(input())
    a = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                if a[i][j] != '-':
                    print('incorrect')
                    return
            else:
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
Suggestion 7

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

n = int(input())
a = []
for i in range(n):
    a.append(list(input()))

=======
Suggestion 8

def check_correctness(n, a):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i][j] == "W":
                if a[j][i] != "L":
                    return False
            elif a[i][j] == "L":
                if a[j][i] != "W":
                    return False
            else:
                if a[j][i] != "D":
                    return False
    return True

n = int(input())
a = [input() for _ in range(n)]

=======
Suggestion 9

def is_correct(n, a):
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

n = int(input())
a = [input() for _ in range(n)]
print("correct" if is_correct(n, a) else "incorrect")

=======
Suggestion 10

def main():
    n = int(input())
    a = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            if a[i][j] == 'W':
                if a[j][i] != 'L':
                    print('incorrect')
                    return
            if a[i][j] == 'L':
                if a[j][i] != 'W':
                    print('incorrect')
                    return
            if a[i][j] == 'D':
                if a[j][i] != 'D':
                    print('incorrect')
                    return
    print('correct')
main()
