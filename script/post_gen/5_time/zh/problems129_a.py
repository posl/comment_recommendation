Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    p,q,r = map(int,input().split())
    print(min(p+q,q+r,r+p))

=======
Suggestion 2

def main():
    p,q,r = map(int,input().split())
    print(min(p+q,q+r,r+p))

=======
Suggestion 3

def main():
    p,q,r = map(int,input().split())
    print(min(p+q,min(q+r,r+p)))

=======
Suggestion 4

def time_calc(p,q,r):
    return min(p+q,q+r,r+p)

p,q,r = map(int,input().split())
print(time_calc(p,q,r))

=======
Suggestion 5

def get_min_route_time(p,q,r):
    times = []
    times.append(p+q)
    times.append(q+r)
    times.append(r+p)
    return min(times)

=======
Suggestion 6

def main():
    p,q,r = [int(x) for x in input().split()]
    print(min(p+q,q+r,r+p))

=======
Suggestion 7

def min(a,b):
    if a > b:
        return b
    else:
        return a
