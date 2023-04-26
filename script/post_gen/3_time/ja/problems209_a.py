Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if A > B:
        print(0)
    else:
        print(B - A + 1)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print(B - A + 1)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print(b - a + 1)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    result = 0
    for i in range(a, b+1):
        if a <= i <= b:
            result += 1
    print(result)

=======
Suggestion 5

def main():
    # A, B = map(int, input().split())
    A, B = map(int, input().split())
    print(B - A + 1)
