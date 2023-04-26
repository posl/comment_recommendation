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

def main():
    r, D, x2000 = map(int, input().split())
    x = x2000
    for i in range(10):
        x = r * x - D
        print(x)

=======
Suggestion 3

def growth(r, D, x):
    return r * x - D

r, D, x = map(int, input().split())

for i in range(10):
    x = growth(r, D, x)
    print(x)

=======
Suggestion 4

def main():
    r,D,x = map(int,input().split())
    for i in range(10):
        x = r*x-D
        print(x)
    return

=======
Suggestion 5

def growth(r, D, x):
    return r * x - D

=======
Suggestion 6

def get_x(r, D, x):
    return r * x - D
