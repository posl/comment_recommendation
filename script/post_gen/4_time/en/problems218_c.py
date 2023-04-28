Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == "#":
                Sx, Sy = i, j
            if T[i][j] == "#":
                Tx, Ty = i, j
    dx, dy = Tx - Sx, Ty - Sy
    for i in range(N):
        for j in range(N):
            if 0 <= i + dx < N and 0 <= j + dy < N:
                if S[i][j] != T[i + dx][j + dy]:
                    print("No")
                    return
    print("Yes")

=======
Suggestion 2

def read_input():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    return N, S, T

=======
Suggestion 3

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        T.append(input())
    for i in range(N):
        for j in range(N):
            if S[i][j] == '#':
                a = i
                b = j
                break
    for i in range(N):
        for j in range(N):
            if T[i][j] == '#':
                c = i
                d = j
                break
    for i in range(N):
        for j in range(N):
            if (a - c + i) < 0 or (a - c + i) >= N or (b - d + j) < 0 or (b - d + j) >= N or S[a - c + i][b - d + j] != T[i][j]:
                break
        else:
            continue
        break
    else:
        print('Yes')
        return
    for i in range(N):
        for j in range(N):
            if (a - c + i) < 0 or (a - c + i) >= N or (b - d + j) < 0 or (b - d + j) >= N or S[a - c + i][b - d + j] != T[N - 1 - j][i]:
                break
        else:
            continue
        break
    else:
        print('Yes')
        return
    for i in range(N):
        for j in range(N):
            if (a - c + i) < 0 or (a - c + i) >= N or (b - d + j) < 0 or (b - d + j) >= N or S[a - c + i][b - d + j] != T[N - 1 - i][N - 1 - j]:
                break
        else:
            continue
        break
    else:
        print('Yes')
        return
    for i in range(N):
        for j in range(N):
            if (a - c + i) < 0 or (a - c + i) >= N or (b - d + j) < 0 or (b - d + j) >= N or S[a - c + i][b - d + j]

=======
Suggestion 4

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        T.append(input())
    for i in range(4):
        if S == T:
            print("Yes")
            exit()
        S = rotate(S)
    print("No")

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    S = [s for s in S if '#' in s]
    T = [t for t in T if '#' in t]
    if len(S) != len(T) or len(S[0]) != len(T[0]):
        print('No')
        return
    for i in range(N):
        for j in range(N):
            if S[0][0] == T[i][j]:
                if all(S[k] == T[k + i][j:j + len(S[0])] for k in range(len(S))):
                    print('Yes')
                    return
    print('No')

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]

    def check(S, T):
        for i in range(N):
            for j in range(N):
                if S[i][j] != T[i][j]:
                    return False
        return True

    def rotate(S):
        return [''.join([S[N-1-j][i] for j in range(N)]) for i in range(N)]

    def translate(S, a, b):
        return [''.join([S[i-a][j-b] for j in range(N)]) for i in range(N)]

    for a in range(N):
        for b in range(N):
            if check(translate(rotate(S), a, b), T):
                print('Yes')
                return
    print('No')

=======
Suggestion 7

def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]

    def check(i, j):
        for k in range(N):
            for l in range(N):
                if S[k][l] == '#':
                    if T[(k + i) % N][(l + j) % N] != '#':
                        return False
        return True

    for i in range(N):
        for j in range(N):
            if check(i, j):
                print('Yes')
                return

    print('No')

=======
Suggestion 8

def  main():
    n = int(input())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(n)]
    for _ in range(4):
        s = rotate(s, n)
        if s == t:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 9

def rotate ( grid ): 
     N = len ( grid ) 
     return [ [ grid [ N - 1 - j ][ i ] for j in range ( N )] for i in range ( N )] 

 def translate ( grid ,  dx ,  dy ): 
     N = len ( grid ) 
     return [ [ grid [ ( i + dx ) % N ][ ( j + dy ) % N ] for j in range ( N )] for i in range ( N )] 

 def solve ( grid1 ,  grid2 ): 
     N = len ( grid1 ) 
     for dx in range ( N ): 
         for dy in range ( N ): 
             for _ in range ( 4 ): 
                 if  grid1  ==  grid2 : 
                     return  True 
                 grid1  =  rotate ( grid1 ) 
             grid1  =  translate ( grid1 ,  dx ,  dy ) 
     return  False 

 N  = int ( input ()) 
 grid1  = [ list ( input ()) for _ in range ( N )] 
 grid2  = [ list ( input ()) for _ in range ( N )] 

 print ( 'Yes'   if  solve ( grid1 ,  grid2 )   else   'No' )

=======
Suggestion 10

def get_shapes(grid):
    shapes = []
    for row in grid:
        for col in row:
            if col == "#":
                shapes.append((row.index(col), grid.index(row)))
                break
    return shapes
