Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int,input().split())
    print(str(a)*b if str(a)*b < str(b)*a else str(b)*a)

=======
Suggestion 2

def main():
    a,b = map(int,input().split())
    if a <= b:
        print(str(a)*b)
    else:
        print(str(b)*a)

main()

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a > b:
        print(str(b)*a)
    else:
        print(str(a)*b)

=======
Suggestion 4

def solve():
    a,b = map(int, input().split())
    if a == b:
        print(str(a)*a)
    elif a > b:
        print(str(b)*a)
    else:
        print(str(a)*b)
solve()

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    a = str(a)
    b = str(b)
    a = a * int(b)
    b = b * int(a)
    print(min(a,b))

=======
Suggestion 6

def main():
    a = int(input())
    b = int(input())
    if a == b:
        print(str(a) * a)
    elif a > b:
        print(str(b) * a)
    else:
        print(str(a) * b)

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    if a < b:
        print(str(a)*b)
    elif a > b:
        print(str(b)*a)
    else:
        print(str(a)*b)

=======
Suggestion 8

def main():
    a,b = map(int,input().split())
    if a < b:
        print(str(a) * b)
    else:
        print(str(b) * a)
