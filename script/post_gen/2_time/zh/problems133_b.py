Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,a,b = map(int, input().split())
    print(min(n*a,b))

=======
Suggestion 2

def main():
    n,a,b = map(int,input().split())
    if n*a < b:
        print(n*a)
    else:
        print(b)

=======
Suggestion 3

def min_cost(n,a,b):
    return min(n*a,b)

=======
Suggestion 4

def minCost(a, b, n):
    return min(a * n, b)

=======
Suggestion 5

def main():
    n,a,b = map(int,input().split())
    if a*n < b:
        print(a*n)
    else:
        print(b)

=======
Suggestion 6

def calc_min_travel_cost(n, a, b):
    cost = 0
    if a * n < b:
        cost = a * n
    else:
        cost = b
    return cost
