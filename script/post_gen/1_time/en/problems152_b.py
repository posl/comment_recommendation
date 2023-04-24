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

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a < b:
        print(str(a)*b)
    else:
        print(str(b)*a)

main()

=======
Suggestion 4

def main():
    a, b = [int(x) for x in input().split()]
    if a < b:
        print(str(a) * b)
    else:
        print(str(b) * a)

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if a > b:
        print(str(b) * a)
    else:
        print(str(a) * b)
main()

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print(min(str(a) * b, str(b) * a))

=======
Suggestion 7

def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a > b:
        print(str(b) * a)
    else:
        print(str(a) * b)
main()

This is the solution I came up with. I am not sure if it is the best way to do it, but it works.

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    print(str(min(a, b)) * max(a, b))
