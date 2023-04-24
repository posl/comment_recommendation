Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if i % 2 == 0:
                        if k % 2 == 0:
                            print('.', end='')
                        else:
                            print('#', end='')
                    else:
                        if k % 2 == 0:
                            print('#', end='')
                        else:
                            print('.', end='')
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
                print('')
        print('')

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if (i+k)%2 == 0:
                        print("#",end="")
                    else:
                        print(".",end="")
                print("")
        print("")

=======
Suggestion 4

def main():
    N,A,B = map(int,input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if (i+k)%2==0:
                        print('.',end='')
                    else:
                        print('#',end='')
                # print()
            print()
        # print()
    return 0

=======
Suggestion 5

def main():
    n,a,b = map(int, input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i+j)%2 == 0:
                        print('#', end='')
                    else:
                        print('.', end='')
                print('', end='')
            print('')
        print('')

=======
Suggestion 6

def main():
    n,a,b = map(int,input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i%2==0 and k%2==0) or (i%2==1 and k%2==1):
                        print("#",end="")
                    else:
                        print(".",end="")
                #print("")
            print("")
        #print("")
    #print("")

=======
Suggestion 7

def main():
    N,A,B = map(int, input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if (i+k)%2 == 0:
                        print('.', end='')
                    else:
                        print('#', end='')
                print()
        print()

=======
Suggestion 8

def main():
    import sys
    N,A,B = map(int, sys.stdin.readline().strip().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if (i+k)%2 == 0:
                        sys.stdout.write('.')
                    else:
                        sys.stdout.write('#')
                sys.stdout.write('\n')
        sys.stdout.write('\n')

=======
Suggestion 9

def main():
    n,a,b = map(int,input().split())
    for i in range(n):
        if i%2==0:
            for j in range(a):
                if j%2==0:
                    for k in range(b):
                        if k%2==0:
                            print(".",end="")
                        else:
                            print("#",end="")
                else:
                    for k in range(b):
                        if k%2==0:
                            print("#",end="")
                        else:
                            print(".",end="")
                print("")
        else:
            for j in range(a):
                if j%2==0:
                    for k in range(b):
                        if k%2==0:
                            print("#",end="")
                        else:
                            print(".",end="")
                else:
                    for k in range(b):
                        if k%2==0:
                            print(".",end="")
                        else:
                            print("#",end="")
                print("")

=======
Suggestion 10

def main():
    N,A,B = map(int,input().split())
    for i in range(N*A):
        if i%N < N//2:
            print("."*(N*B))
        else:
            print("#"*(N*B))
