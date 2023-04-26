Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a <= b:
        print(0)
    else:
        print(a-b*2)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A <= B:
        print(0)
    else:
        print(A - B * 2)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a < b:
        print(0)
    else:
        print(a - b * 2)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    print(max(0, a - 2 * b))

=======
Suggestion 5

def main():
    A,B = map(int,input().split())
    if A > B:
        print(0)
    else:
        print(B-A)

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print(max(a - 2*b, 0))

=======
Suggestion 7

def main():
    a, b = map(int, input().split())

    print(max(0, a - 2 * b))

main()

=======
Suggestion 8

def main():
    a,b = map(int,input().split())
    print(max(0,a-b*2))
