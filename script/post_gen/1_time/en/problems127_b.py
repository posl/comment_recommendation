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

def algae(r, D, x):
    for i in range(10):
        x = r * x - D
        print(x)

r, D, x = map(int, input().split())
algae(r, D, x)

=======
Suggestion 3

def algae():
    r, D, x = map(int, input().split())
    for i in range(10):
        x = r*x - D
        print(x)

=======
Suggestion 4

def algae(r, D, x):
    for i in range(10):
        x = r * x - D
        print(x)

=======
Suggestion 5

def calc_algo(r, D, x):
    return r*x - D
