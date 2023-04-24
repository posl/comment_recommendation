Synthesizing 10/10 solutions

=======
Suggestion 1

def print_grid(N, A, B):
    for i in range(A*N):
        for j in range(B*N):
            if (i//A + j//B) % 2 == 0:
                print('.', end='')
            else:
                print('#', end='')
        print()

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    for i in range(a):
        for j in range(n):
            for k in range(b):
                if ((i + j) % 2 == 0):
                    print('.', end='')
                else:
                    print('#', end='')
            if (j != n - 1):
                print('.', end='')
        print()

=======
Suggestion 3

def print_tile(n, a, b):
    for i in range(a):
        for j in range(n):
            if (i + j) % 2 == 0:
                print('.' * b, end='')
            else:
                print('#' * b, end='')
        print()

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    for i in range(A):
        for j in range(N):
            if j % 2 == 0:
                print((".#"*B)[:B], end="")
            else:
                print(("#."*B)[:B], end="")
        print()
    for i in range(N):
        for j in range(A):
            if i % 2 == 0:
                print((".#"*B)[:B], end="")
            else:
                print(("#."*B)[:B], end="")
        print()

=======
Suggestion 5

def main():
    N, A, B = (int(x) for x in input().split())
    for i in range(A*N):
        if i % A == 0:
            for j in range(B*N):
                if j % B == 0:
                    if (i//A) % 2 == 0:
                        if (j//B) % 2 == 0:
                            print('.', end='')
                        else:
                            print('#', end='')
                    else:
                        if (j//B) % 2 == 0:
                            print('#', end='')
                        else:
                            print('.', end='')
                else:
                    print('.', end='')
        else:
            for j in range(B*N):
                if j % B == 0:
                    if (i//A) % 2 == 0:
                        if (j//B) % 2 == 0:
                            print('#', end='')
                        else:
                            print('.', end='')
                    else:
                        if (j//B) % 2 == 0:
                            print('.', end='')
                        else:
                            print('#', end='')
                else:
                    print('#', end='')
        print()

=======
Suggestion 6

def get_tiles(n, a, b):
    tiles = []
    for i in range(n):
        for j in range(n):
            if i % 2 == 0:
                if j % 2 == 0:
                    tiles.append(['.'] * b)
                else:
                    tiles.append(['#'] * b)
            else:
                if j % 2 == 0:
                    tiles.append(['#'] * b)
                else:
                    tiles.append(['.'] * b)
    return tiles

=======
Suggestion 7

def get_tile(N, A, B):
    tile = [['.' for i in range(B)] for j in range(A)]
    for i in range(A):
        for j in range(B):
            if (i + j) % 2 == 0:
                tile[i][j] = '#'
    return tile

=======
Suggestion 8

def make_tiles(n, a, b):
    tiles = []
    for i in range(n):
        for j in range(n):
            if i%2 == 0:
                if j%2 == 0:
                    tiles.append(['#']*b)
                else:
                    tiles.append(['.']*b)
            else:
                if j%2 == 0:
                    tiles.append(['.']*b)
                else:
                    tiles.append(['#']*b)
    return tiles

=======
Suggestion 9

def  solve ( N ,  A ,  B ):
    ans  =  [ [ 0  for  _  in  range ( B * N )]  for  _  in  range ( A * N )]
     for  i  in  range ( N ):
         for  j  in  range ( N ):
             for  k  in  range ( A ):
                 for  l  in  range ( B ):
                    ans [ A * i + k ][ B * j + l ] =  ( i + j + k + l )  %  2 
     for  i  in  range ( A * N ):
         for  j  in  range ( B * N ):
            ans [ i ][ j ] =  '.'   if  ans [ i ][ j ] ==  0   else  '#'
         print ( '' . join ( ans [ i ]))

=======
Suggestion 10

def printBoard(board):
    for row in board:
        print("".join(row))
