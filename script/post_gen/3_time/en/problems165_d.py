Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, N = map(int, input().split())
    if B <= N:
        x = B - 1
    else:
        x = N
    print(A * x // B - A * (x // B))

=======
Suggestion 2

def main():
    A, B, N = map(int, input().split())
    if N < B:
        x = N
    else:
        x = B - 1
    print((A * x) // B - A * (x // B))

=======
Suggestion 3

def main():
    A, B, N = map(int, input().split())
    if N < B-1:
        x = N
    else:
        x = B-1
    print((A*x)//B - A*(x//B))

=======
Suggestion 4

def main():
    A, B, N = map(int, input().split())
    if B <= N:
        x = B - 1
    else:
        x = N
    print((A*x)//B - A*(x//B))

=======
Suggestion 5

def main():
    a, b, n = map(int, input().split())
    if n >= b:
        x = b - 1
    else:
        x = n
    print((a * x) // b - a * (x // b))

=======
Suggestion 6

def main():
    A,B,N = map(int,input().split())
    if N < B-1:
        x = N
    else:
        x = B-1
    ans = (A*x)//B - A*(x//B)
    print(ans)

=======
Suggestion 7

def main():
    A, B, N = map(int, input().split())
    if N >= B-1:
        print(A*(B-1)//B)
    else:
        print(A*N//B)

=======
Suggestion 8

def main():
    A, B, N = map(int, input().split())
    if N < B:
        print(int(A*N/B))
    else:
        print(int(A*(B-1)/B))

=======
Suggestion 9

def main():
    A,B,N = map(int, input().split())
    if N >= B-1:
        x = B-1
    else:
        x = N
    print(A*x//B - A*(x//B))

=======
Suggestion 10

def main():
    A, B, N = map(int, input().split())
    print(A * min(N, B-1) // B)
