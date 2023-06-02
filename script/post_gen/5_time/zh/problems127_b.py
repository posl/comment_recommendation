Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    r, D, x = map(int, input().split())
    for i in range(10):
        x = r * x - D
        print(x)

=======
Suggestion 2

def get_next_year_weight(r, D, weight):
    return r * weight - D

=======
Suggestion 3

def main():
    r, D, x2000 = map(int, input().split())
    for i in range(10):
        x2000 = r * x2000 - D
        print(x2000)

=======
Suggestion 4

def pond(r,D,x):
    for i in range(10):
        x = r*x - D
        print(x)

r,D,x = map(int,input().split())
pond(r,D,x)

=======
Suggestion 5

def get_x(r, D, x):
    return r * x - D

=======
Suggestion 6

def main():
    # r D x_2000
    r, D, x = map(int, input().split())
    for i in range(10):
        x = r * x - D
        print(x)

=======
Suggestion 7

def get_next(x, r, D):
    return r * x - D

r, D, x = map(int, input().split())
for i in range(10):
    x = get_next(x, r, D)
    print(x)
