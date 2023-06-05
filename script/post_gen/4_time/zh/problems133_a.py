Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, a, b = map(int, input().split())
    print(min(n*a, b))

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    print(min(A*N, B))

=======
Suggestion 3

def min_travel_cost(N, A, B):
    return min(N * A, B)

=======
Suggestion 4

def minCost(n, a, b):
    return min(n * a, b)

=======
Suggestion 5

def main():
    N,A,B = map(int, input().split())
    if N*A < B:
        print(N*A)
    else:
        print(B)

=======
Suggestion 6

def main():
    N,A,B = map(int,input().split())
    print(min(N*A,B))

=======
Suggestion 7

def solution():
    N,A,B = map(int,input().split())
    print(min(N*A,B))
