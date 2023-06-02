Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A,B = map(int,input().split())
    if B%A == 0:
        print(B//A)
    else:
        print(B//A+1)

=======
Suggestion 2

def main():
    A,B = map(int, input().split())
    if B % A == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 3

def main():
    A,B = map(int,input().split())
    if B%A == 0:
        print(int(B/A))
    else:
        print(int(B/A)+1)

=======
Suggestion 4

def split_input(input_str):
    return input_str.split()

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if b % a == 0:
        print(b // a - 1)
    else:
        print(b // a)

=======
Suggestion 6

def solve():
    A,B = map(int,input().split())
    if B%A==0:
        print(B//A)
    else:
        print(B//A+1)

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    if b%a == 0:
        print(int(b/a))
    else:
        print(int(b/a)+1)

=======
Suggestion 8

def get_input():
    a,b = input().split()
    return a,b

=======
Suggestion 9

def cal(a,b):
    if a == 1:
        return 0
    if b <= a:
        return 1
    if b % a == 0:
        return int(b/a)
    else:
        return int(b/a)+1

=======
Suggestion 10

def main():
    a, b = map(int, input().split())
    if b % a == 0:
        print(b // a)
    else:
        print(b // a + 1)
