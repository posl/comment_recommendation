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
    if a < b:
        print(str(a) * b)
    else:
        print(str(b) * a)

main()

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a < b:
        print(str(a) * b)
    else:
        print(str(b) * a)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a > b:
        print(str(b) * a)
    else:
        print(str(a) * b)

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if a > b:
        print(str(a) * b)
    else:
        print(str(b) * a)

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    if a == b:
        print(str(a) * a)
    else:
        print(str(min(a, b)) * max(a, b))

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    print(min(str(a)*b, str(b)*a))

=======
Suggestion 8

def main():
    a,b = map(int,input().split())
    if a==b:
        print(str(a)*b)
    else:
        if a<b:
            print(str(a)*b)
        else:
            print(str(b)*a)
