Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int,input().split())
    if str(a)*b < str(b)*a:
        print(str(a)*b)
    else:
        print(str(b)*a)

=======
Suggestion 2

def main():
    a, b = input().split()
    if a * int(b) < b * int(a):
        print(a * int(b))
    else:
        print(b * int(a))

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print(min(str(a) * b, str(b) * a))

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    a = str(a)*b
    b = str(b)*a
    if a<b:
        print(a)
    else:
        print(b)

=======
Suggestion 5

def main():
    a,b = map(int, input().split())
    a = str(a)
    b = str(b)
    if a * b < b * a:
        print(a * b)
    else:
        print(b * a)

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if a*b == 0:
        print(0)
        return
    if a < b:
        print(str(a)*b)
    else:
        print(str(b)*a)

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    if a*b == 0:
        return
    if str(a)*b < str(b)*a:
        print(str(a)*b)
    else:
        print(str(b)*a)

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    if a * b == 0:
        print(0)
    elif a * b < 10:
        print(a * b)
    elif a * b > 10:
        print(str(a) * b)

=======
Suggestion 9

def main():
    a,b = map(int,input().split())
    if a*b == 0:
        print(0)
    else:
        print(min(str(a)*b,str(b)*a))
