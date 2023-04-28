Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a < b:
        print(str(a) * b)
    else:
        print(str(b) * a)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a > b:
        print(str(b) * a)
    else:
        print(str(a) * b)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print(str(a) * b if a < b else str(b) * a)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a < b:
        print(a * 10 ** b)
    else:
        print(b * 10 ** a)

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print(min(str(a)*b, str(b)*a))

=======
Suggestion 6

def solve():
    a,b = map(int,input().split())
    print(str(a)*b if a < b else str(b)*a)
