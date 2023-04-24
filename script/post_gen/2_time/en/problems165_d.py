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

=======
Suggestion 2

def main():
    a, b, n = map(int, input().split())
    if b - 1 <= n:
        print((a * (b - 1)) // b)
    else:
        print((a * n) // b)

=======
Suggestion 3

def main():
    A, B, N = map(int, input().split())
    x = min(N, B-1)
    print((A*x)//B - A*(x//B))

main()

=======
Suggestion 4

def main():
    A, B, N = map(int, input().split())
    x = min(B-1, N)
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
    a, b, n = map(int, input().split())
    if n < b:
        print(a * n // b)
    else:
        print(a * (b - 1) // b)

=======
Suggestion 7

def main():
    A, B, N = map(int, input().split())
    if B-1 <= N:
        print(A*(B-1)//B)
    else:
        print(A*N//B)

=======
Suggestion 8

def main():
    A, B, N = map(int, input().split())
    if N < B:
        print(A * N // B)
        return
    else:
        print(A * (B - 1) // B)
        return

=======
Suggestion 9

def main():
    A, B, N = map(int, input().split())
    if A >= B:
        print(B-1)
        return
    if N >= B-1:
        print(A*(B-1)//B)
        return
    print(A*N//B)

=======
Suggestion 10

def solve():
    A,B,N = map(int,input().split())
    X = min(N,B-1)
    ans = A*X//B - A*(X//B)
    print(ans)
solve()
