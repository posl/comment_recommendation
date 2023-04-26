Synthesizing 10/10 solutions

=======
Suggestion 1

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
    return

=======
Suggestion 2

def main():
    N = int(input())
    A = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                if A[i][j] != '-':
                    print("incorrect")
                    exit()
            else:
                if A[i][j] == 'W' and A[j][i] != 'L':
                    print("incorrect")
                    exit()
                elif A[i][j] == 'L' and A[j][i] != 'W':
                    print("incorrect")
                    exit()
                elif A[i][j] == 'D' and A[j][i] != 'D':
                    print("incorrect")
                    exit()
    print("correct")
main()

=======
Suggestion 3

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
    print('correct')
    return

=======
Suggestion 4

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
                    print('incorrect')
                    return
            elif a[i][j] == 'L':
                if a[j][i] != 'W':
                    print('incorrect')
                    return
            elif a[i][j] == 'D':
                if a[j][i] != 'D':
                    print('incorrect')
                    return
    print('correct')

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(input()))
    for i in range(N):
        A[i][i] = '-'
    for i in range(N):
        for j in range(N):
            if A[i][j] == 'W':
                if A[j][i] != 'L':
                    print('incorrect')
                    exit()
            elif A[i][j] == 'L':
                if A[j][i] != 'W':
                    print('incorrect')
                    exit()
            elif A[i][j] == 'D':
                if A[j][i] != 'D':
                    print('incorrect')
                    exit()
    print('correct')

=======
Suggestion 6

def main():
    N = int(input())
    A = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and A[i][j] == "W" and A[j][i] != "L":
                print("incorrect")
                return
            if i != j and A[i][j] == "L" and A[j][i] != "W":
                print("incorrect")
                return
            if i != j and A[i][j] == "D" and A[j][i] != "D":
                print("incorrect")
                return
    print("correct")
main()

=======
Suggestion 7

def main():
    N = int(input())
    A = [input() for i in range(N)]
    flag = True
    for i in range(N):
        for j in range(N):
            if A[i][j] == 'W':
                if A[j][i] != 'L':
                    flag = False
            elif A[i][j] == 'L':
                if A[j][i] != 'W':
                    flag = False
            elif A[i][j] == 'D':
                if A[j][i] != 'D':
                    flag = False
    if flag:
        print('correct')
    else:
        print('incorrect')

=======
Suggestion 8

def main():
    # input
    n = int(input())
    a = [list(input()) for _ in range(n)]

    # compute
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            elif a[i][j] == 'W':
                if a[j][i] != 'L':
                    print('incorrect')
                    return
            elif a[i][j] == 'L':
                if a[j][i] != 'W':
                    print('incorrect')
                    return
            elif a[i][j] == 'D':
                if a[j][i] != 'D':
                    print('incorrect')
                    return

    # output
    print('correct')

=======
Suggestion 9

def check(input):
    for i in range(len(input)):
        for j in range(len(input)):
            if input[i][j] == 'W':
                if input[j][i] != 'L':
                    return False
            elif input[i][j] == 'L':
                if input[j][i] != 'W':
                    return False
            elif input[i][j] == 'D':
                if input[j][i] != 'D':
                    return False
    return True

=======
Suggestion 10

def check(a,b):
    if a == "W":
        return b == "L"
    elif a == "L":
        return b == "W"
    else:
        return b != "D"

n = int(input())
a = [input() for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if a[i][j] == "-":
            continue
        if check(a[i][j], a[j][i]) == False:
            print("incorrect")
            exit()
print("correct")
