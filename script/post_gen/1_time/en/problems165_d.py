Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, N = map(int, input().split())
    x = min(N, B - 1)
    print((A * x) // B - A * (x // B))

main()

=======
Suggestion 2

def main():
    A, B, N = map(int, input().split())
    if B - 1 <= N:
        x = B - 1
    else:
        x = N
    print(A * x // B - A * (x // B))

=======
Suggestion 3

def main():
    A, B, N = map(int, input().split())
    if N < B:
        print(A * N // B - A * (N // B))
    else:
        print(A * (B - 1) // B - A * ((B - 1) // B))

=======
Suggestion 4

def main():
    A, B, N = map(int, input().split())
    if N < B-1:
        x = N
    else:
        x = B-1
    print((A*x)//B - A*(x//B))

=======
Suggestion 5

def main():
    A, B, N = map(int, input().split())
    if N < B:
        x = N
    else:
        x = B - 1
    print(A * x // B - A * (x // B))

=======
Suggestion 6

def main():
    A, B, N = map(int, input().split())
    x = min(N, B-1)
    print((A*x)//B - A*(x//B))

=======
Suggestion 7

def main():
    A, B, N = map(int, input().split())
    if N >= B-1:
        x = B-1
    else:
        x = N
    print(int(A*x/B) - A*int(x/B))

=======
Suggestion 8

def main():
    A, B, N = map(int,input().split())
    x = min(B-1, N)
    print(int(A*x/B) - A*int(x/B))

=======
Suggestion 9

def get_input():
    return list(map(int, input().split()))
