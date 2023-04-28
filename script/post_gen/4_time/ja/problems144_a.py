Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a > 9 or b > 9:
        print(-1)
    else:
        print(a*b)

=======
Suggestion 2

def main():
    a,b = map(int,input().split())
    if a >= 1 and a <= 20 and b >= 1 and b <= 20:
        print(a*b)
    else:
        print(-1)

=======
Suggestion 3

def main():
    A,B = map(int,input().split())
    if A > 9 or B > 9:
        print(-1)
    else:
        print(A*B)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a < 1 or a > 20 or b < 1 or b > 20:
        return
    print(a * b)

=======
Suggestion 5

def mul(a,b):
    if a >= 1 and a <= 20 and b >= 1 and b <= 20:
        return a * b
    else:
        return -1

=======
Suggestion 6

def calc(a,b):
    if a < 1 or a > 20 or b < 1 or b > 20:
        return -1
    else:
        return a * b

=======
Suggestion 7

def mult(a, b):
    if a <= 0 or b <= 0:
        return -1
    elif a >= 10 or b >= 10:
        return -1
    else:
        return a * b

=======
Suggestion 8

def get_input_lines():
    while True:
        try:
            yield raw_input()
        except EOFError:
            break
