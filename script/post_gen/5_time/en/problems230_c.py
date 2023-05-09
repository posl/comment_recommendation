Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (i-A) == (j-B):
                print('#', end='')
            elif (i-A) == -(j-B):
                print('#', end='')
            else:
                print('.', end='')
        print('')

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())
    for i in range(p, q + 1):
        for j in range(r, s + 1):
            if (i - a) == (j - b):
                print("#", end="")
            elif (i - a) == -(j - b):
                print("#", end="")
            else:
                print(".", end="")
        print()

main()

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())

    #print(N, A, B)
    #print(P, Q, R, S)

    #print(N, A, B)
    #print(P, Q, R, S)

    print("Hello World!")

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())

    #print(N, A, B)
    #print(P, Q, R, S)

    #print("")

    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (i+j) % 2 == 0:
                print("#", end="")
            else:
                print(".", end="")
        print("")

=======
Suggestion 5

def solve():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    print(N, A, B, P, Q, R, S)
    return

=======
Suggestion 6

def main():
    N,A,B = map(int,input().split())
    P,Q,R,S = map(int,input().split())
    for i in range(P,Q+1):
        for j in range(R,S+1):
            if (i+A+j+B)%2 == 0:
                print('#',end='')
            else:
                print('.',end='')
        print('')

=======
Suggestion 7

def solve():
    N,A,B = map(int,input().split())
    P,Q,R,S = map(int,input().split())
    for i in range(P,Q+1):
        for j in range(R,S+1):
            if (i+j) % 2 == (A+B) % 2:
                print("#",end="")
            else:
                print(".",end="")
        print()

=======
Suggestion 8

def main():
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())
    if (p + q - 1) % 2 == 0:
        print("#" * (s - r + 1))
        for i in range(q - p - 1):
            print("#" + "." * (s - r - 1) + "#")
        print("#" * (s - r + 1))
    else:
        for i in range(q - p + 1):
            if i % 2 == 0:
                print("#" + "." * (s - r) + "#")
            else:
                print("." * (s - r + 1))

=======
Suggestion 9

def paint(N, A, B, P, Q, R, S):
    result = ''
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (i+j)%2 == 0:
                result += '#'
            else:
                result += '.'
        result += '\n'
    return result

=======
Suggestion 10

def paint(n, a, b, p, q, r, s):
    #print(n, a, b, p, q, r, s)
    #print([max(1-a,1-b), min(n-a,n-b)])
    #print([max(1-a,b-n), min(n-a,b-1)])
    #print([max(1-a,1-b), min(n-a,n-b)])
    #print([max(1-a,b-n), min(n-a,b-1)])
    #print([max(1-a,1-b), min(n-a,n-b)])
    #print([max(1-a,b-n), min(n-a,b-1)])
    #print([max(1-a,1-b), min(n-a,n-b)])
    #print([max(1-a,b-n), min(n-a,b-1)])
    #print([max(1-a,1-b), min(n-a,n-b)])
    #print([max(1-a,b-n), min(n-a,b-1)])
    #print([max(1-a,1-b), min(n-a,n-b)])
    #print([max(1-a,b-n), min(n-a,b-1)])
    #print([max(1-a,1-b), min(n-a,n-b)])
    #print([max(1-a,b-n), min(n-a,b-1)])
    #print([max(1-a,1-b), min(n-a,n-b)])
    #print([max(1-a,b-n), min(n-a,b-1)])
    #print([max(1-a,1-b), min(n-a,n-b)])
    #print([max(1-a,b-n), min(n-a,b-1)])
    #print([max(1-a,1-b), min(n-a,n-b)])
    #print([max(1-a,b-n), min(n-a,b-1)])
    
    #print([max(1-a,1-b), min(n-a,n-b)])
    #print([max(1-a,b-n), min(n-a,b-1)])
    #print([max(1-a,1-b), min(n-a,n-b)])
    #print([max(1-a,b-n), min(n-a,b-1)])
    
    #print([max(1-a,1-b), min(n-a,n-b)])
    #print([max(1-a,b-n), min(n-a,b-
