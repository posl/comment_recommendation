Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, a, b = map(int, input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i + k) % 2 == 0:
                        print('.', end='')
                    else:
                        print('#', end='')
                print('', end='')
            print('')
        print('')

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i + k) % 2 == 0:
                        print('.', end='')
                    else:
                        print('#', end='')
                print()
        print()

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if (i + k) % 2 == 0:
                        print(".", end="")
                    else:
                        print("#", end="")
            print()
main()

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if (i + k) % 2 == 0:
                        print('.', end='')
                    else:
                        print('#', end='')
                print()
        print()

=======
Suggestion 5

def main():
    n,a,b = map(int,input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i+k)%2==0:
                        print(".",end="")
                    else:
                        print("#",end="")
                print("",end="")
            print("")
        print("",end="")
    print("")

=======
Suggestion 6

def main():
    N,A,B = map(int,input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if (j+k)%2==0:
                        print('.',end='')
                    else:
                        print('#',end='')
                print()
        print()

=======
Suggestion 7

def main():
    N,A,B = map(int,input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if i%2 == 0 and k%2 == 0:
                        print(".",end="")
                    elif i%2 == 0 and k%2 == 1:
                        print("#",end="")
                    elif i%2 == 1 and k%2 == 0:
                        print("#",end="")
                    elif i%2 == 1 and k%2 == 1:
                        print(".",end="")
                print("",end="")
            print("")
        print("")

=======
Suggestion 8

def main():
    n,a,b = map(int,input().split())
    for i in range(a*n):
        if i%2 == 0:
            print("."*b + "#"*b)
        else:
            print("#"*b + "."*b)

=======
Suggestion 9

def paint_tile(N, A, B):
    tile = [["." for i in range(B*N)] for j in range(A*N)]
    for i in range(A*N):
        for j in range(B*N):
            if i % 2 == 0 and j % 2 == 0:
                tile[i][j] = "#"
            elif i % 2 == 1 and j % 2 == 1:
                tile[i][j] = "#"
    return tile

=======
Suggestion 10

def getTile(n,a,b):
    tile = []
    for i in range(n):
        line = ""
        for j in range(n):
            if (i+j)%2 == 0:
                line += "."*b
            else:
                line += "#"*b
        tile.append(line)
    return tile
