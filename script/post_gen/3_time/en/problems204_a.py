Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    else:
        print(3 - x - y)

=======
Suggestion 2

def main():
    x, y = input().split()
    x = int(x)
    y = int(y)
    z = (x + 1) % 3
    if z == y:
        print(x)
    else:
        print(z)

=======
Suggestion 3

def main():
    x, y = input().split()
    if x == y:
        print(x)
    else:
        print(3 - int(x) - int(y))

main()

=======
Suggestion 4

def main():
    x, y = [int(i) for i in input().split()]
    if x == y:
        print(x)
    else:
        print(3 - x - y)

=======
Suggestion 5

def main():
    x, y = input().split()
    if x == y:
        print(x)
    else:
        print(str(3 - int(x) - int(y)))

=======
Suggestion 6

def main():
    x, y = map(int, input().split())
    print((x + y) % 3)

=======
Suggestion 7

def main():
    x, y = map(int, input().split())
    print(3 - (x + y))

main()

=======
Suggestion 8

def main():
    x, y = map(int, input().split())
    print(3 - x - y)
