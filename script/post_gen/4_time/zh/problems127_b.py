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
    inList = input().split()
    r = int(inList[0])
    D = int(inList[1])
    x = int(inList[2])
    for i in range(10):
        x = r * x - D
        print(x)

=======
Suggestion 3

def f(r, D, x):
    return r * x - D

=======
Suggestion 4

def func(r,D,x):
    for i in range(10):
        x = r*x - D
        print(x)

=======
Suggestion 5

def main():
    r,D,x_2000 = map(int,input().split())
    print(x_2000)
    for i in range(10):
        x_2000 = r*x_2000 - D
        print(x_2000)

=======
Suggestion 6

def algae(r, D, x):
    for i in range(10):
        x = r * x - D
        print(x)

r, D, x = map(int, input().split())
algae(r, D, x)

=======
Suggestion 7

def problem127_b():
    r, D, x_2000 = map(int, input().split())
    x = x_2000
    for i in range(10):
        x = r * x - D
        print(x)

=======
Suggestion 8

def problem127_b():
    r, D, x = map(int, input().split())
    for i in range(10):
        x = r * x - D
        print(x)

problem127_b()
