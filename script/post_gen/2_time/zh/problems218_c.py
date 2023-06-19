Synthesizing 10/10 solutions

=======
Suggestion 1

def rotate90(s):
    return list(zip(*s[::-1]))

=======
Suggestion 2

def rotate90(grid):
    return [''.join([grid[i][j] for i in range(len(grid))]) for j in range(len(grid[0])-1,-1,-1)]

=======
Suggestion 3

def rotate90(grid):
    return list(zip(*grid[::-1]))

=======
Suggestion 4

def get_input():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        t.append(input())
    return n, s, t

=======
Suggestion 5

def rotate90(n,matrix):
    new_matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            new_matrix[j][n-i-1] = matrix[i][j]
    return new_matrix

=======
Suggestion 6

def rotate90(S):
    N = len(S)
    T = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            T[i][j] = S[N-1-j][i]
    return T

=======
Suggestion 7

def rotate_matrix(m):
    return [list(reversed(i)) for i in zip(*m)]

=======
Suggestion 8

def rotate90(m):
    return [list(x) for x in zip(*m[::-1])]

=======
Suggestion 9

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(list(input()))
    for i in range(n):
        t.append(list(input()))
    for i in range(4):
        t = rotate(t)
        if s == t:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 10

def check(S,T):
    #print(S)
    #print(T)
    #print("-----------")
    for i in range(len(S)):
        for j in range(len(S)):
            if S[i][j] != T[i][j]:
                return False
    return True
