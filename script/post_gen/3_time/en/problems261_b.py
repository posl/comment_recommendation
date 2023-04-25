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
                if A[i][j] != '-':
                    print('incorrect')
                    return
            elif A[i][j] == 'W' and A[j][i] != 'L':
                print('incorrect')
                return
            elif A[i][j] == 'L' and A[j][i] != 'W':
                print('incorrect')
                return
            elif A[i][j] == 'D' and A[j][i] != 'D':
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
                if A[i][j] != '-':
                    print('incorrect')
                    return
            else:
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
main()

=======
Suggestion 4

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

=======
Suggestion 5

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
Suggestion 6

def main():
    N = int(input())
    A = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
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
Suggestion 7

def main():
    N = int(input())
    A = [input() for _ in range(N)]
    ans = "correct"
    for i in range(N):
        for j in range(N):
            if i == j:
                if A[i][j] != "-":
                    ans = "incorrect"
                    break
            else:
                if A[i][j] == "W":
                    if A[j][i] != "L":
                        ans = "incorrect"
                        break
                elif A[i][j] == "L":
                    if A[j][i] != "W":
                        ans = "incorrect"
                        break
                elif A[i][j] == "D":
                    if A[j][i] != "D":
                        ans = "incorrect"
                        break
    print(ans)

main()

=======
Suggestion 8

def main():
    n = int(input())
    a = [input() for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            if a[i][j] == "W" and a[j][i] != "L":
                print("incorrect")
                return
            elif a[i][j] == "L" and a[j][i] != "W":
                print("incorrect")
                return
            elif a[i][j] == "D" and a[j][i] != "D":
                print("incorrect")
                return

    print("correct")

=======
Suggestion 9

def main():
    n = int(input())
    a = [input() for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
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
Suggestion 10

def check(A):
    for i in range(len(A)):
        if A[i][i] != '-':
            return False
        for j in range(len(A)):
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
A = [input() for _ in range(N)]
