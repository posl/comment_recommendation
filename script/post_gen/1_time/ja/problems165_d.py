Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, N = map(int, input().split())
    if B - 1 <= N:
        x = B - 1
    else:
        x = N
    print((A * x) // B - A * (x // B))

main()

=======
Suggestion 2

def main():
    A, B, N = map(int, input().split())
    if N < B:
        print((A * N) // B - A * (N // B))
    else:
        print((A * (B - 1)) // B - A * ((B - 1) // B))

=======
Suggestion 3

def main():
    A, B, N = map(int, input().split())
    if N >= B-1:
        x = B-1
    else:
        x = N
    ans = (A*x)//B - A*(x//B)
    print(ans)

=======
Suggestion 4

def main():
    A,B,N = map(int,input().split())
    if B-1 <= N:
        x = B-1
    else:
        x = N
    print((A*x)//B - A*(x//B))

=======
Suggestion 5

def main():
    A, B, N = map(int, input().split())
    x = min(N, B-1)
    print((A*x)//B - A*(x//B))

=======
Suggestion 6

def main():
    A, B, N = map(int, input().split())
    if B <= N:
        X = B-1
    else:
        X = N
    print((A*X)//B - A*(X//B))

=======
Suggestion 7

def main():
    A,B,N = map(int,input().split())
    if B-1 <= N:
        x = B-1
    else:
        x = N
    print(A*x//B-A*(x//B))

=======
Suggestion 8

def main():
    A,B,N = map(int,input().split())
    if N >= B:
        x = B-1
    else:
        x = N
    print((A*x)//B - A*(x//B))

=======
Suggestion 9

def main():
    A,B,N = map(int,input().split())
    if N >= B-1:
        print(A*(B-1)//B)
    else:
        print(A*N//B)

=======
Suggestion 10

def main():
    A,B,N = map(int,input().split())
    if N >= B-1:
        print((A*(B-1))//B)
    else:
        print((A*N)//B)
