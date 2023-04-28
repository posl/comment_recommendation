Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a < b:
        print(str(a) * b)
    else:
        print(str(b) * a)

=======
Suggestion 2

def main():
    a, b = [int(x) for x in input().split()]
    if (str(a)*b) < (str(b)*a):
        print(str(a)*b)
    else:
        print(str(b)*a)
    return

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print(min(str(a)*b, str(b)*a))

=======
Suggestion 4

def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a < b:
        print(str(a)*b)
    else:
        print(str(b)*a)
    return

main()

=======
Suggestion 5

def main():
    a, b = input().split()
    if int(a+b) < int(b+a):
        print(a*b)
    else:
        print(b*a)

=======
Suggestion 6

def main():
    a = int(input())
    b = int(input())
    if a > b:
        print(str(b) * a)
    else:
        print(str(a) * b)

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    print(min([str(a)*b, str(b)*a]))

=======
Suggestion 8

def main():
    a,b = input().split()
    if a*b > b*a:
        print(b*a)
    else:
        print(a*b)

=======
Suggestion 9

def main():
    a,b=list(map(int,input().split()))
    print(str(a)*b if str(a)*b<str(b)*a else str(b)*a)
