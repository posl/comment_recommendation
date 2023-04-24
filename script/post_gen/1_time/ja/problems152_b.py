Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if str(a) * b < str(b) * a:
        print(str(a) * b)
    else:
        print(str(b) * a)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print(min(str(a) * b, str(b) * a))

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a * b > 0:
        print(min(str(a) * b, str(b) * a))
    else:
        print(max(str(a) * b, str(b) * a))

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    if a<b:
        print(str(a)*b)
    else:
        print(str(b)*a)

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if a * b == 0:
        print(0)
        return
    elif a < b:
        print(str(a) * b)
    elif a > b:
        print(str(b) * a)
    else:
        print(str(a) * b)

=======
Suggestion 6

def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a * b > 0:
        if a < b:
            print(a * b)
        else:
            print(a * b)
    else:
        print("0")

=======
Suggestion 7

def main():
    a,b = map(int,input().split())

    if a > b:
        print(str(a)*b)
    else:
        print(str(b)*a)

=======
Suggestion 8

def main():
    a,b = map(int,input().split())
    if a*b < a+b:
        print(str(a)*b)
    else:
        print(str(b)*a)
