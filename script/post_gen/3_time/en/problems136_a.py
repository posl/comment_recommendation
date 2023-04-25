Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    if C >= A - B:
        print(C - (A - B))
    else:
        print(C)

=======
Suggestion 2

def main():
    A, B, C = [int(x) for x in input().split()]
    if A - B >= C:
        print(0)
    else:
        print(C - (A - B))

=======
Suggestion 3

def main():
    A, B, C = map(int, input().split())
    if (C - (A - B)) >= 0:
        print(C - (A - B))
    else:
        print(0)

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    print(max(0, C - (A - B)))

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    print(c - (a - b) if c - (a - b) > 0 else 0)

=======
Suggestion 6

def main():
    A, B, C = map(int, input().split(' '))
    if C - (A - B) > 0:
        print(C - (A - B))
    else:
        print(0)

=======
Suggestion 7

def main():
    A, B, C = map(int, input().split())
    print(max(C - (A - B), 0))

=======
Suggestion 8

def main():
    # Write your code here
    A,B,C = map(int,input().split())
    if C >= A-B:
        print(C-(A-B))
    else:
        print(C)
