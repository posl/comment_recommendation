Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int,input().split())
    if a <= b:
        print(0)
    else:
        print(a-b*2)

=======
Suggestion 2

def main():
    a,b = map(int,input().split())
    if a <= b:
        print(0)
    else:
        print(a-b)

=======
Suggestion 3

def problems143_a():
    a, b = map(int, input().split())
    if a < b:
        print(0)
    else:
        print(a - b)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a > b:
        print(a - b)
    else:
        print(0)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    if A <= B:
        print(0)
    else:
        print(A - B * 2)

=======
Suggestion 6

def func(a, b):
    if a <= b:
        return 0
    else:
        return a - b

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    print(max(0, A - 2 * B))

=======
Suggestion 8

def calc_remainder_of_window(A, B):
    if A <= B:
        return 0
    else:
        return A - B * 2

=======
Suggestion 9

def problem143_a():
    a,b = map(int, input().split())
    print(max(0, a-2*b))

problem143_a()
