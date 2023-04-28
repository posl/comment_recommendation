Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    else:
        print(3 - x - y)

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    else:
        print(3 - (x + y))

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    print(3 - x - y)
