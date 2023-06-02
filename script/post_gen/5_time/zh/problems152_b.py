Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a > b:
        print(str(b) * a)
    elif a < b:
        print(str(a) * b)
    else:
        print(str(a) * b)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a < b:
        print(str(a)*b)
    else:
        print(str(b)*a)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a == b:
        print(str(a) * a)
    elif a > b:
        print(str(b) * a)
    else:
        print(str(a) * b)

=======
Suggestion 4

def problem152_b():
    a, b = map(int, input().split())
    if a >= b:
        print(str(b) * a)
    else:
        print(str(a) * b)

problem152_b()

=======
Suggestion 5

def main():
    a,b = input().split()
    a = int(a)
    b = int(b)
    if a < b:
        print(str(a)*b)
    else:
        print(str(b)*a)

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if a < b:
        for i in range(b):
            print(a,end='')
    else:
        for i in range(a):
            print(b,end='')
    print()

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    if a == b:
        print(str(a) * b)
    elif a > b:
        print(str(b) * a)
    else:
        print(str(a) * b)
