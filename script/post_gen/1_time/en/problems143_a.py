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
    a, b = map(int, input().split())
    if a > b:
        print(a-b)
    else:
        print(0)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print(max(0, a - 2 * b))

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    print(0 if a >= b else b - a)

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    print(max(0,a-b*2))

=======
Suggestion 6

def main():
    # Take input
    a, b = map(int, input().split())

    # Calculate the answer
    ans = a - 2 * b

    # Print the answer
    print(ans)

=======
Suggestion 7

def solution(a,b):
    if a > b:
        return a - b*2
    else:
        return 0
