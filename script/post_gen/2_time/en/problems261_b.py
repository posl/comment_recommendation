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
            if A[i][j] == 'W':
                if A[j][i] != 'L':
                    print('incorrect')
                    return
            elif A[i][j] == 'L':
                if A[j][i] != 'W':
                    print('incorrect')
                    return
            else:
                if A[j][i] != 'D':
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
                if A[i][j] != '-':
                    print('incorrect')
                    return
            else:
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
Suggestion 3

def main():
    N = int(input())
    A = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                if A[i][j] != "-":
                    print("incorrect")
                    return
            else:
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
Suggestion 4

def main():
    N = int(input())
    A = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                if A[i][j] != '-':
                    print('incorrect')
                    return
            else:
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
                else:
                    print('incorrect')
                    return
    print('correct')

=======
Suggestion 5

def main():
    n = int(input())
    a = [input() for _ in range(n)]
    ans = 'correct'
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'W' and a[j][i] == 'L':
                ans = 'incorrect'
            if a[i][j] == 'L' and a[j][i] == 'W':
                ans = 'incorrect'
            if a[i][j] == 'D' and a[j][i] == 'D':
                ans = 'incorrect'
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if A[i][j] == 'W' and A[j][i] == 'L':
                print('incorrect')
                return
            if A[i][j] == 'L' and A[j][i] == 'W':
                print('incorrect')
                return
            if A[i][j] == 'D' and A[j][i] == 'D':
                print('incorrect')
                return
    print('correct')

=======
Suggestion 7

def check(A):
    N = len(A)
    for i in range(N):
        for j in range(N):
            if i == j:
                if A[i][j] != '-':
                    return False
            else:
                if A[i][j] == 'W' and A[j][i] != 'L':
                    return False
                if A[i][j] == 'L' and A[j][i] != 'W':
                    return False
                if A[i][j] == 'D' and A[j][i] != 'D':
                    return False
    return True

N = int(input())
A = []
for i in range(N):
    A.append(input())

=======
Suggestion 8

def main():
    N = int(input())
    table = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                if table[i][j] != "-":
                    print("incorrect")
                    return
            else:
                if table[i][j] == "W":
                    if table[j][i] != "L":
                        print("incorrect")
                        return
                elif table[i][j] == "L":
                    if table[j][i] != "W":
                        print("incorrect")
                        return
                else:
                    if table[j][i] != "D":
                        print("incorrect")
                        return
    print("correct")
    return

main()

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
            if a[i][j] == 'W' and a[j][i] == 'L':
                continue
            if a[i][j] == 'L' and a[j][i] == 'W':
                continue
            if a[i][j] == 'D' and a[j][i] == 'D':
                continue
            print('incorrect')
            return

    print('correct')

=======
Suggestion 10

def solve():
    n = int(input())
    a = [list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'W':
                if a[j][i] == 'L':
                    return 'incorrect'
            elif a[i][j] == 'L':
                if a[j][i] == 'W':
                    return 'incorrect'
            elif a[i][j] == 'D':
                if a[j][i] == 'D':
                    return 'incorrect'
    return 'correct'

print(solve())
