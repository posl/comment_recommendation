Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if A <= B * 2:
        print(0)
    else:
        print(A - B * 2)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if b * 2 > a:
        print(0)
    else:
        print(a - b * 2)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print(max(0, a - 2 * b))

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    print(max(0, A - 2 * B))

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    if B >= A:
        print(0)
    else:
        print(A - B - B)

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    print(max(A - B - B, 0))
