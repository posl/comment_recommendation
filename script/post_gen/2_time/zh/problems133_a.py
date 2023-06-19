Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def min_cost(n, a, b):
    cost = 0
    if n * a < b:
        cost = n * a
    else:
        cost = b
    return cost

=======
Suggestion 2

def main():
    N,A,B=map(int,input().split())
    print(min(N*A,B))

=======
Suggestion 3

def main():
    n, a, b = map(int, input().split())
    print(min(n * a, b))

=======
Suggestion 4

def get_min_cost(n, a, b):
    if n*a < b:
        return n*a
    else:
        return b

=======
Suggestion 5

def main():
    n, a, b = map(int, input().split())
    print(min(a*n, b))

=======
Suggestion 6

def min_travel_cost(n, a, b):
    return n * a if n * a < b else b

=======
Suggestion 7

def min_travel_cost(n, a, b):
    return min(n*a, b)

=======
Suggestion 8

def min_cost(n, a, b):
    return min(n*a, b)

=======
Suggestion 9

def main():
    n, a, b = map(int, input().split())
    if (n * a) < b:
        print(n * a)
    else:
        print(b)
