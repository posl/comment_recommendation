Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [input() for _ in range(N)]
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
            if A[i][j] == 'D' and A[j][i] != 'D':
                print('incorrect')
                return
    print('correct')

=======
Suggestion 2

def main():
    N = int(input())
    A = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == "W" and A[j][i] != "L":
                print("incorrect")
                return
            if A[i][j] == "L" and A[j][i] != "W":
                print("incorrect")
                return
            if A[i][j] == "D" and A[j][i] != "D":
                print("incorrect")
                return
    print("correct")

=======
Suggestion 3

def main():
    n = int(input())
    a = [input() for _ in range(n)]
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
    N = int(input())
    A = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == 'W' and A[j][i] != 'L':
                print('incorrect')
                return
            elif A[i][j] == 'L' and A[j][i] != 'W':
                print('incorrect')
                return
            elif A[i][j] == 'D' and A[j][i] != 'D':
                print('incorrect')
                return
    print('correct')
    return

=======
Suggestion 5

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
Suggestion 6

def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(input()))
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
    return

=======
Suggestion 7

def solve():
    N = int(input())
    A = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            if A[i][j] == "W" and A[j][i] != "L":
                return "incorrect"
            elif A[i][j] == "L" and A[j][i] != "W":
                return "incorrect"
            elif A[i][j] == "D" and A[j][i] != "D":
                return "incorrect"
    return "correct"

print(solve())

=======
Suggestion 8

def is_contradictory(N, A):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == 'W' and A[j][i] != 'L':
                return True
            if A[i][j] == 'L' and A[j][i] != 'W':
                return True
            if A[i][j] == 'D' and A[j][i] != 'D':
                return True
    return False

N = int(input())
A = [input() for _ in range(N)]

=======
Suggestion 9

def main():
    n = int(input())
    result = [input() for i in range(n)]
    for i in range(n):
        for j in range(n):
            if result[i][j] == 'W':
                if result[j][i] != 'L':
                    print('incorrect')
                    return
            if result[i][j] == 'L':
                if result[j][i] != 'W':
                    print('incorrect')
                    return
            if result[i][j] == 'D':
                if result[j][i] != 'D':
                    print('incorrect')
                    return
    print('correct')

=======
Suggestion 10

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())

    result = 'correct'
    for i in range(N):
        for j in range(N):
            if i != j:
                if A[i][j] == 'W':
                    if A[j][i] != 'L':
                        result = 'incorrect'
                elif A[i][j] == 'L':
                    if A[j][i] != 'W':
                        result = 'incorrect'
                elif A[i][j] == 'D':
                    if A[j][i] != 'D':
                        result = 'incorrect'
    print(result)

main()
