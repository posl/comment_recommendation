Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

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
Suggestion 3

def main():
    N = int(input())
    A = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
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
main()

=======
Suggestion 4

def main():
    N = int(input())
    A = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
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
Suggestion 5

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
                if A[i][j] == "W":
                    if A[j][i] != "L":
                        print("incorrect")
                        return
                elif A[i][j] == "L":
                    if A[j][i] != "W":
                        print("incorrect")
                        return
                elif A[i][j] == "D":
                    if A[j][i] != "D":
                        print("incorrect")
                        return
    print("correct")

=======
Suggestion 6

def main():
    N = int(input())
    A = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j: continue
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
Suggestion 7

def main():
    N = int(input())
    A = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
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

main()

=======
Suggestion 8

def solve():
    N = int(input())
    A = [input() for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                if A[i][j] != "-":
                    return "incorrect"
            else:
                if A[i][j] == "W" and A[j][i] != "L":
                    return "incorrect"
                if A[i][j] == "L" and A[j][i] != "W":
                    return "incorrect"
                if A[i][j] == "D" and A[j][i] != "D":
                    return "incorrect"
    return "correct"

=======
Suggestion 9

def check(a):
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
            return False
    return True
n = int(input())
a = [list(input()) for _ in range(n)]
print('correct' if check(a) else 'incorrect')

The solution is based on the observation that if the given table is not contradictory, then:

Player i beat Player j, if and only if Player j lost to Player i;

Player i lost to Player j, if and only if Player j beat Player i;

Player i drew with Player j, if and only if Player j drew with Player i.

So, the solution is to check if the above conditions hold for all i and j.

The solution is written in Python 3.6.5.

import sys
input = sys.stdin.readline
n = int(input())
a = [input() for _ in range(n)]
ans = 'correct'
for i in range(n):
    for j in range(n):
        if i == j:
            if a[i][j] != '-':
                ans = 'incorrect'
        else:
            if a[i][j] == 'W' and a[j][i] != 'L':
                ans = 'incorrect'
            if a[i][j] == 'L' and a[j][i] != 'W':
                ans = 'incorrect'
            if a[i][j] == 'D' and a[j][i] != 'D':
                ans = 'incorrect'
print(ans)

The solution is based on the observation that if the given table is not contradictory, then:

Player i beat Player j, if and only if Player j lost to Player i;

Player i lost to Player j, if and only if Player j beat Player i;

Player i drew with Player j, if and only if Player j drew with Player i.

So, the solution is to check if the above conditions hold for all i and j.

The solution is written in Python 3.6.5.
