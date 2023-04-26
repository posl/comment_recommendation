Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, N = map(int, input().split())
    if B <= N:
        x = B - 1
    else:
        x = N
    print((A * x) // B - A * (x // B))

=======
Suggestion 2

def main():
    A, B, N = map(int, input().split())
    if B-1 <= N:
        print((A*(B-1))//B - A*((B-1)//B))
    else:
        print((A*N)//B - A*(N//B))

=======
Suggestion 3

def main():
    A, B, N = map(int, input().split())
    if B > N:
        print((A * N) // B)
    else:
        print((A * (B - 1)) // B)

=======
Suggestion 4

def main():
    A,B,N = map(int,input().split())
    if N<B-1:
        print((A*N)//B - A*((N)//B))
    else:
        print((A*(B-1))//B - A*((B-1)//B))

=======
Suggestion 5

def main():
    A, B, N = map(int, input().split())
    if N < B:
        print(A*N//B)
    else:
        print(A*(B-1)//B)

=======
Suggestion 6

def main():
    a,b,n = map(int,input().split())
    if b-1 <= n:
        print((a*(b-1)//b)-a*((b-1)//b))
    else:
        print((a*n//b)-a*(n//b))

=======
Suggestion 7

def main():
    A, B, N = map(int, input().split())
    x = min(B-1, N)
    print(A*x//B)

=======
Suggestion 8

def main():
    A, B, N = map(int, input().split())
    # print(A, B, N)
    if B <= N:
        x = B - 1
    else:
        x = N
    print(A * x // B - A * (x // B))

=======
Suggestion 9

def main():
    import sys
    readline = sys.stdin.readline
    A, B, N = map(int, readline().split())
    if N < B:
        print((A*N)//B)
    else:
        print((A*(B-1))//B)

=======
Suggestion 10

def main():
    A,B,N = map(int,input().split())
    print(A*min(B-1,N)//B)
