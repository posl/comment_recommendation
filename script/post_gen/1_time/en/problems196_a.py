Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(b - c, d - a))

=======
Suggestion 2

def main():
    a, b = [int(x) for x in input().split()]
    c, d = [int(x) for x in input().split()]
    print(max(abs(a-c), abs(a-d), abs(b-c), abs(b-d)))
main()

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(b-d, a-c))

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    if b <= c or d <= a:
        print(0)
    else:
        print(max(b, d) - min(a, c))

=======
Suggestion 5

def main():
    a,b = [int(x) for x in input().split()]
    c,d = [int(x) for x in input().split()]
    print(max(b-d,a-c))

=======
Suggestion 6

def main():
    #input
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    #output
    print(max(b - c, d - a))
