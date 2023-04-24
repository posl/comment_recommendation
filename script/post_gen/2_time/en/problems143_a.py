Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a < b * 2:
        print(0)
    else:
        print(a - b * 2)

main()

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a >= 2 * b:
        print(a - 2 * b)
    else:
        print(0)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if A <= B:
        print(0)
    else:
        print(A - B)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a <= b*2:
        print(0)
    else:
        print(a-(b*2))

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print(max(0, a - 2*b))

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    print(max(0, A - 2 * B))

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    print(max(0, A - B * 2))

=======
Suggestion 8

def main():
    A, B = map(int, input().split())
    print(max(A - B * 2, 0))

=======
Suggestion 9

def main():
    a,b = map(int, input().split())
    print(max(a-b*2,0))
