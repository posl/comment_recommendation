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
    a, b = input().split()
    if a * int(b) < b * int(a):
        print(a * int(b))
    else:
        print(b * int(a))

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
        print(str(a) * b)
    else:
        print(str(b) * a)

main()

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if a == b:
        print(str(a)*a)
    elif a > b:
        print(str(b)*b)
    else:
        print(str(a)*a)

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print(min(str(a)*b, str(b)*a))

=======
Suggestion 7

def main():
    a, b = input().split()
    if int(a) > int(b):
        print(b * int(a))
    else:
        print(a * int(b))

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    print(min(str(a)*b, str(b)*a))
main()

a, b = map(int, input().split())
print(min(str(a)*b, str(b)*a))
