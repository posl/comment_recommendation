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

def get_x_i(r, D, x_i):
    return r * x_i - D

=======
Suggestion 3

def main():
    r, D, x2000 = map(int, input().split())
    for i in range(10):
        x2000 = r * x2000 - D
        print(x2000)

=======
Suggestion 4

def print_x(r, D, x):
    for i in range(10):
        x = r * x - D
        print(x)

r, D, x = map(int, input().split())
print_x(r, D, x)

=======
Suggestion 5

def main():
    r, D, x = map(int, input().split())
    for i in range(1, 11):
        x = r * x - D
        print(x)

=======
Suggestion 6

def problem127_b():
    r,D,x_2000 = map(int,input().split())

    for i in range(10):
        x_2000 = r*x_2000 - D
        print(x_2000)

problem127_b()

=======
Suggestion 7

def main():
    r, D, x = map(int, input().split())
    for _ in range(10):
        x = r * x - D
        print(x)
