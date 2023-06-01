Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,a,b = map(int,input().split())
    for i in range(n*a):
        if i%a == 0:
            for j in range(n*b):
                if j%b == 0:
                    print("#",end="")
                else:
                    print(".",end="")
            print("")
        else:
            for j in range(n*b):
                if j%b == 0:
                    print(".",end="")
                else:
                    print("#",end="")
            print("")

=======
Suggestion 2

def main():
    N,A,B = map(int, input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if (i+j)%2 == 0:
                        print("#", end='')
                    else:
                        print(".", end='')
                print("", end='')
            print("")
        print("")

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def print_tile(a,b):
    for i in range(a):
        if i%2==0:
            print("#"*b,end="")
        else:
            print("."*b,end="")
        print()
    return

=======
Suggestion 5

def problems250_b(n, a, b):
    #print(n, a, b)
    for i in range(a*n):
        for j in range(b*n):
            if (i//a + j//b) % 2 == 0:
                print('.', end='')
            else:
                print('#', end='')
        print()

=======
Suggestion 6

def main():
    n, a, b = map(int, input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i + j) % 2 == 0:
                        print("#", end="")
                    else:
                        print(".", end="")
            print()
        print()

=======
Suggestion 7

def main():
    n,a,b = map(int,input().split())
    #n = int(n)
    #a = int(a)
    #b = int(b)
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i+j)%2 == 0:
                        print('.',end='')
                    else:
                        print('#',end='')
            print()
main()

=======
Suggestion 8

def print_tile(n,a,b):
    n = int(n)
    a = int(a)
    b = int(b)
    for i in range(a*n):
        for j in range(b*n):
            if ((i//a)+(j//b))%2 == 0:
                print('.',end='')
            else:
                print('#',end='')
        print('')

=======
Suggestion 9

def problems250_b():
    pass
