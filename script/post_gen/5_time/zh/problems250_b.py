Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problem250_b():
    pass

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if (i + j) % 2 == 0:
                        print('.', end='')
                    else:
                        print('#', end='')
                print()
        print()

=======
Suggestion 3

def main():
    N,A,B = map(int,input().split())
    for i in range(A*N):
        for j in range(B*N):
            if (i//N+j//B)%2==0:
                print('.',end='')
            else:
                print('#',end='')
        print()

=======
Suggestion 4

def main():
    n,a,b = [int(x) for x in input().split()]
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i+j)%2==0:
                        print(".",end="")
                    else:
                        print("#",end="")
                print("",end="")
            print("")
        print("")

=======
Suggestion 5

def main():
    N,A,B = map(int, input().split())
    for i in range(A*N):
        for j in range(B*N):
            if i%2==0:
                if j%2==0:
                    print('.',end='')
                else:
                    print('#',end='')
            else:
                if j%2==0:
                    print('#',end='')
                else:
                    print('.',end='')
        print('')

=======
Suggestion 6

def print_tile(n, a, b):
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i + j) % 2 == 0:
                        print('.', end='')
                    else:
                        print('#', end='')
                print('', end='')
            print('')
        print('')

=======
Suggestion 7

def problems250_b(n,a,b):
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i+j)%2==0 and (k+l)%2==0:
                        print('.',end='')
                    elif (i+j)%2==0 and (k+l)%2!=0:
                        print('#',end='')
                    elif (i+j)%2!=0 and (k+l)%2==0:
                        print('#',end='')
                    elif (i+j)%2!=0 and (k+l)%2!=0:
                        print('.',end='')
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
            print()
        print()

=======
Suggestion 9

def print_tile(n,a,b):
    for i in range(a):
        for j in range(n):
            for k in range(b):
                if (i+j)%2==0:
                    if k==0:
                        print('.',end='')
                    else:
                        print('#',end='')
                else:
                    if k==0:
                        print('#',end='')
                    else:
                        print('.',end='')
            print('')
        print('')

n,a,b=map(int,input().split())
print_tile(n,a,b)
