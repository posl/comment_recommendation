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
    r, D, x_2000 = map(int, input().split())
    for i in range(10):
        x_2000 = r * x_2000 - D
        print(x_2000)

=======
Suggestion 3

def main():
    r, D, x2000 = map(int, input().split())
    for i in range(10):
        x = r * x2000 - D
        print(x)
        x2000 = x

=======
Suggestion 4

def main():
    r, D, x2000 = map(int, input().split())
    for i in range(2000, 2010):
        x = r * x2000 - D
        print(x)
        x2000 = x

=======
Suggestion 5

def main():
    r, D, x = map(int, input().split())
    for _ in range(10):
        x = r*x - D
        print(x)
