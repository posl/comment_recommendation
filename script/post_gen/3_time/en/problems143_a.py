Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a >= b * 2:
        print(a - b * 2)
    else:
        print(0)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if b >= a:
        print(0)
    else:
        print(a - b)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a <= b:
        print(0)
    else:
        print(a - b)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    print(max(0, a - 2 * b))

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print(max(a - 2 * b, 0))

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    print(max(0, A - 2 * B))

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    print(max(0, A - B * 2))

=======
Suggestion 8

def main():
    A, B = map(int, input().split())
    print((A - B) if (A - B) > 0 else 0)

=======
Suggestion 9

def main():
    # Write your code here
    a,b = map(int,input().split())
    if a > b*2:
        print(a-b*2)
    else:
        print(0)
