Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int,input().split())
    if a > 9 or b > 9:
        print(-1)
    else:
        print(a*b)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if (A > 0 and A < 21) and (B > 0 and B < 21):
        print(A * B)
    else:
        print(-1)

=======
Suggestion 3

def main():
    a,b = map(int,input().split())
    if a <= 20 and b <= 20:
        print(a*b)
    else:
        print(-1)

=======
Suggestion 4

def main():
    input = raw_input()
    inputs = input.split()
    a = int(inputs[0])
    b = int(inputs[1])
    if a > 9 or b > 9:
        print -1
    else:
        print a * b

=======
Suggestion 5

def main():
    a,b = map(int, input().split())
    if 1 <= a and a <= 20 and 1 <= b and b <= 20:
        print(a*b)
    else:
        print(-1)

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if (a > 0 and a < 21) and (b > 0 and b < 21):
        print(a*b)
    else:
        print(-1)
