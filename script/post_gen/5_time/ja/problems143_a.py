Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print(max(0, a - 2 * b))

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    ans = a - b * 2
    if ans < 0:
        ans = 0
    print(ans)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print(a - b * 2 if a >= b * 2 else 0)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a <= b:
        print(0)
    else:
        print(a-b*2)

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

def get_min_visible_width(w, c):
    return max(0, w - 2 * c)

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    if a > b:
        print(a-b*2)
    else:
        print(0)

=======
Suggestion 8

def solve():
    a, b = map(int, input().split())
    print(max(0, a - 2 * b))
