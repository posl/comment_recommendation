Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

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

=======
Suggestion 3

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
                print('', end='')
            print('')
        print('')

=======
Suggestion 4

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
    return

=======
Suggestion 5

def print_grid(n, a, b):
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
Suggestion 6

def paint_tile(a, b):
    for i in range(a):
        for j in range(b):
            if (i + j) % 2 == 0:
                print('.', end='')
            else:
                print('#', end='')
        print()

=======
Suggestion 7

def print_pattern(a,b):
    for i in range(a):
        for j in range(b):
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

n,a,b=map(int,input().split())
for i in range(n):
    print_pattern(a,b)

=======
Suggestion 8

def main():
    input = raw_input()
    input = input.split()
    N = int(input[0])
    A = int(input[1])
    B = int(input[2])
    for i in range(0,N):
        for j in range(0,A):
            for k in range(0,N):
                if (i+j)%2==0:
                    for l in range(0,B):
                        print ".",
                else:
                    for l in range(0,B):
                        print "#",
            print ""
    return 0

=======
Suggestion 9

def main():
    # get input
    n, a, b = map(int, input().split())
    # print output
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
Suggestion 10

def main():
    # Get input here
    n,a,b = [int(x) for x in input().strip().split()]
    # Calculate result here
    result = 0
    # Print output here
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i+k)%2==0:
                        print(".",end="")
                    else:
                        print("#",end="")
                print("")
    return 0
