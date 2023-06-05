Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print(2*a+100-b)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if B <= 2 * A:
        print(2 * A - B)
    else:
        print(0)

=======
Suggestion 3

def solution():
    a, b = map(int, input().split())
    print(a*2+100-b)

solution()

=======
Suggestion 4

def main():
    A,B = map(int,input().split())
    if B <= 2 * A + 100:
        print(2 * A + 100 - B)
    else:
        print(0)

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if b <= 2 * a + 100:
        print(2 * a + 100 - b)
    else:
        print(0)
