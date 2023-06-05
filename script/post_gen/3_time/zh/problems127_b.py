Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def calc(r, D, x):
    return r * x - D

=======
Suggestion 2

def get_x(r, D, x):
    return r * x - D

=======
Suggestion 3

def solve(r, D, x_2000):
    for i in range(10):
        x_2000 = r * x_2000 - D
        print(x_2000)

=======
Suggestion 4

def main():
    r,D,x = map(int,input().split())
    for i in range(10):
        x = r*x - D
        print(x)

=======
Suggestion 5

def problems127_b():
    r, D, x = map(int, input().split())
    for i in range(10):
        x = r * x - D
        print(x)

=======
Suggestion 6

def sum(i,r):
    if i > 2000:
        return r*sum(i-1,r)-10
    else:
        return 20

=======
Suggestion 7

def f(r, D, x):
    return r * x - D
