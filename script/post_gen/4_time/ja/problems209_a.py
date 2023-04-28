Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a > b:
        print(0)
    else:
        print(b - a + 1)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a >= b:
        print(0)
    else:
        print(b - a + 1)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if A > B:
        print(0)
    else:
        print(B - A + 1)

main()

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    print(b - a + 1 if b - a >= 0 else 0)

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print(b - a + 1 if b > a else 0)

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print(b-a+1 if b >= a else 0)

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    print(b-a+1 if b-a+1 > 0 else 0)

=======
Suggestion 8

def main():
    A, B = map(int, input().split())
    print(B - A + 1)

=======
Suggestion 9

def main():
    # n = int(input())
    # s = input()
    # n, k = map(int, input().split())
    a, b = map(int, input().split())
    # a = list(map(int, input().split()))
    # s = input()
    # n, m = map(int, input().split())
    # a = list(map(int, input().split()))
    # s = input()
    # a = int(input())
    if b < a:
        print(0)
    else:
        print(b-a+1)
