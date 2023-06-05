Synthesizing 10/10 solutions

=======
Suggestion 1

def print_tile(n, a, b):
    for i in range(a * n):
        for j in range(b * n):
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
        print('')

=======
Suggestion 2

def solve(n, a, b):
    pass

=======
Suggestion 3

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
Suggestion 4

def main():
    n,a,b = map(int,input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i+j)%2 == 0:
                        print('.',end='')
                    else:
                        print('#',end='')
                print('',end='')
            print('')
        print('')

=======
Suggestion 5

def main():
    n,a,b = map(int,input().split())
    for i in range(a*n):
        for j in range(b*n):
            if i%2==0:
                if j%2==0:
                    print(".",end="")
                else:
                    print("#",end="")
            else:
                if j%2==0:
                    print("#",end="")
                else:
                    print(".",end="")
        print("")

=======
Suggestion 6

def main():
    n,a,b = map(int, input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if ((i+j)%2 == 0):
                        print('.', end='')
                    else:
                        print('#', end='')
                print('', end='')
            print('')
        print('')

=======
Suggestion 7

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
                print('')
        print('')

=======
Suggestion 8

def main():
    n, a, b = map(int, input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i + j) % 2 == 0:
                        print('.', end='')
                    else:
                        print('#', end='')
                print('')
        print('')

=======
Suggestion 9

def main():
    n,a,b=map(int,raw_input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i+j)%2==0:
                        print '.',
                    else:
                        print '#',
                print
            print
main()

=======
Suggestion 10

def problems250_b():
    return None
