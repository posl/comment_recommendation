Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(b-c)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(a-c, a-d, b-c, b-d))

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(a * c, a * d, b * c, b * d))

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(a-c, a-d, b-c, b-d))
main()

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(b - c)
    return

=======
Suggestion 6

def main():
    a,b = map(int, input().split())
    c,d = map(int, input().split())

    print(b-d)

=======
Suggestion 7

def solve(a, b, c, d):
    return max(a * c, a * d, b * c, b * d)
