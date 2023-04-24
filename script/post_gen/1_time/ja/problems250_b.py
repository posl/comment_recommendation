Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    for i in range(A * N):
        for j in range(B * N):
            if (i // N + j // N) % 2 == 0:
                print('.', end='')
            else:
                print('#', end='')
        print()

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    for i in range(A * N):
        for j in range(B * N):
            if (i // A + j // B) % 2 == 0:
                print('.', end='')
            else:
                print('#', end='')
        print()

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    for i in range(A):
        for j in range(B):
            for k in range(N):
                if (i + j) % 2 == 0:
                    print('.', end='')
                else:
                    print('#', end='')
        print()

=======
Suggestion 4

def main():
    n, a, b = map(int, input().split())
    for i in range(a):
        for j in range(n):
            for k in range(b):
                for l in range(n):
                    if (i + j + k + l) % 2 == 0:
                        print("#", end="")
                    else:
                        print(".", end="")
            print()
    return

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())

    for i in range(A):
        for j in range(N):
            for k in range(B):
                for l in range(N):
                    if (i + j + k + l) % 2 == 0:
                        print('.', end='')
                    else:
                        print('#', end='')
            print()

=======
Suggestion 6

def main():
    N,A,B = map(int,input().split())
    for i in range(A*N):
        for j in range(B*N):
            if (i//A+j//B)%2 == 0:
                print(".",end="")
            else:
                print("#",end="")
        print()

=======
Suggestion 7

def main():
    n,a,b = map(int,input().split())
    for i in range(a):
        for j in range(n):
            for k in range(b):
                for l in range(n):
                    if (i+j+k+l)%2 == 0:
                        print(".",end="")
                    else:
                        print("#",end="")
            print()

=======
Suggestion 8

def main():
    N, A, B = map(int, input().split())

    for i in range(A):
        for j in range(B):
            if (i + j) % 2 == 0:
                for k in range(N):
                    print('.' * N, end='')
            else:
                for k in range(N):
                    print('#' * N, end='')
        print('')

=======
Suggestion 9

def main():
    N, A, B = map(int, input().split())
    for i in range(1, A * N + 1):
        for j in range(1, B * N + 1):
            if  ((i - 1) // A + (j - 1) // B) % 2 == 0:
                print("#", end="")
            else:
                print(".", end="")
        print()
