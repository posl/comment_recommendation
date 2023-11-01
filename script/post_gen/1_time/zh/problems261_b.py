Synthesizing 10/10 solutions

=======
Suggestion 1

def check(x, y):
    if a[x][y] == "D":
        return True
    elif a[x][y] == "W":
        return not check(y, x)
    elif a[x][y] == "L":
        return check(y, x)
    else:
        return False

=======
Suggestion 2

def check(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == "W":
                if a[j][i] != "L":
                    return False
            elif a[i][j] == "L":

=======
Suggestion 3

def main():
    N = int(input())
    A = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                pass
            elif A[i][j] == 'W' and A[j][i] != 'L':

=======
Suggestion 4

def check(n, a):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i][j] == 'W' and a[j][i] != 'L':
                return False

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(input()))
    for i in range(n):
        for j in range(i+1,n):
            if a[i][j] == 'W' and a[j][i] != 'L':

=======
Suggestion 6

def check(table, N):
    for i in range(N):
        for j in range(N):
            if table[i][j] == 'W':
                if table[j][i] != 'L':
                    return False
            elif table[i][j] == 'L':
                if table[j][i] != '

=======
Suggestion 7

def main():
    N = int(input())
    A = [input() for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == 'W':

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    for i in range(n):
        if a[i][i] != '-':
            print('incorrect')
            return
        for j in range(i+1, n):

=======
Suggestion 9

def check(i,j):
    #print("i=",i,"j=",j)
    #print("A[i][j]=",A[i][j])
    #print("A[j][i]=",A[j][i])
    if A[i][j] == "W":
        if A[j][i] != "L":
            return False
    elif A[i][j] ==

=======
Suggestion 10

def judge(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if(i==j):
                continue
            if(a[i][j] == 'W' and a[j][i] != 'L'):
                return False
            if(a[i][j] == 'L' and
