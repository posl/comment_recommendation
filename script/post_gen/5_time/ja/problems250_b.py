Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n, a, b):
    ans = []
    for i in range(n):
        if i < n//2:
            ans.append("."*b + "#"*b)
        else:
            ans.append("#"*b + "."*b)
    return ans

=======
Suggestion 2

def main():
    N,A,B = map(int,input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if (i + k) % 2 == 0:
                        print(".",end="")
                    else:
                        print("#",end="")
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
                        print('.', end='')
                    else:
                        print('#', end='')
                print()
        print()

=======
Suggestion 4

def main():
    N,A,B = map(int,input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if (i+k)%2==0:
                        print("#",end="")
                    else:
                        print(".",end="")
                print("",end="")
            print("")
        print("")

=======
Suggestion 5

def main():
    N,A,B = map(int, input().split())
    
    for i in range(A*N):
        for j in range(B*N):
            if (i//N+j//N)%2==0:
                print(".",end="")
            else:
                print("#",end="")
        print("")

=======
Suggestion 6

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
            print("")
main()

=======
Suggestion 7

def main():
    n,a,b = map(int,input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i+k)%2==0:
                        print('#',end='')
                    else:
                        print('.',end='')
                print()
        print()

=======
Suggestion 8

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
Suggestion 9

def main():
    N,A,B = map(int,input().split())
    for i in range(N):
        for j in range(N):
            if i < A:
                if j < B:
                    print('.',end='')
                else:
                    print('#',end='')
            else:
                if j < B:
                    print('#',end='')
                else:
                    print('.',end='')
        print()

=======
Suggestion 10

def main():
    N,A,B = map(int,input().split())
    for i in range(A*N):
        for j in range(B*N):
            if (j//B+i//A)%2==0:
                print(".",end="")
            else:
                print("#",end="")
        print("")
