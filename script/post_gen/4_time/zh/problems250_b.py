Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def print_tile(a, b):
    for i in range(a):
        for j in range(b):
            if (i + j) % 2 == 0:
                print('#', end='')
            else:
                print('.', end='')
        print()

=======
Suggestion 3

def printAB(a,b):
    for i in range(a):
        for j in range(b):
            if (i+j)%2==0:
                print("#",end="")
            else:
                print(".",end="")
        print("")

=======
Suggestion 4

def problems250_b():
    n,a,b = map(int,input().split())
    for i in range(n * a):
        for j in range(n * b):
            if (i // a + j // b) % 2 == 0:
                print(".",end="")
            else:
                print("#",end="")
        print()

=======
Suggestion 5

def main():
    n,a,b = map(int,input().strip().split())
    for i in range(0,n):
        for j in range(0,a):
            for k in range(0,n):
                for l in range(0,b):
                    if (i+j)%2==0:
                        print('.',end='')
                    else:
                        print('#',end='')
            print('')
    return

=======
Suggestion 6

def print_tile(A, B):
    for i in range(A):
        for j in range(B):
            if (i+j)%2 == 0:
                print('#', end='')
            else:
                print('.', end='')
        print('')

=======
Suggestion 7

def main():
    n, a, b = map(int, input().split())
    for i in range(n * a):
        for j in range(n * b):
            if (i // a + j // b) % 2 == 0:
                print('.', end='')
            else:
                print('#', end='')
        print()

=======
Suggestion 8

def main():
    N,A,B = map(int, input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if i % 2 == 0:
                        if j % 2 == 0:
                            print('.', end='')
                        else:
                            print('#', end='')
                    else:
                        if j % 2 == 0:
                            print('#', end='')
                        else:
                            print('.', end='')
                print()
main()
