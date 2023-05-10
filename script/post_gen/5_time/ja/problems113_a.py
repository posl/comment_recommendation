Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x,y = map(int, input().split())
    print(x + y//2)

=======
Suggestion 2

def main():
    x,y = map(int, input().split())
    if y % 2 == 0:
        print(x * (y//2))
    else:
        print("error")

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    if y % 2 == 0:
        print(x * (y // 2))
    else:
        print(-1)

=======
Suggestion 4

def main():
    X, Y = map(int, input().split())

    print(X + int(Y / 2))

main()

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    print(int(x + y/2))

=======
Suggestion 6

def main():
    x, y = map(int, input().split())
    print(x + int(y / 2))

=======
Suggestion 7

def main():
    X, Y = map(int, input().split())
    print(int(X + Y/2))
