Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a > 9 or b > 9:
        print(-1)
    else:
        print(a * b)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if 1 <= a <= 9 and 1 <= b <= 9:
        print(a*b)
    else:
        print(-1)

main()

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a <= 9 and b <= 9:
        print(a * b)
    else:
        print(-1)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a < 10 and b < 10:
        print(a * b)
    else:
        print(-1)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    if A <= 9 and B <= 9:
        print(A * B)
    else:
        print(-1)

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    if A < 10 and B < 10:
        print(A * B)
    else:
        print(-1)

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    print(a * b if a <= 9 and b <= 9 else -1)

=======
Suggestion 8

def main():
    #input
    A,B = map(int,input().split())
    #calculation
    if A > 9 or B > 9:
        print(-1)
    else:
        print(A*B)
    #output
