Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # input
    A, B, C = map(int, input().split())

    # compute

    # output
    print(max(10 * A + B + C, A + 10 * B + C, A + B + 10 * C))

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    print(a + b + c + max(a, b, c) * 9)

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    print(max(a+b+c, a+b*c, a*b+c, a*b*c))

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    print(max(A+B+C, A+B*C, A*B+C, A*B*C))

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    print(max(a+b+c, a+b*c, a*b+c, a*b*c))

main()

=======
Suggestion 6

def main():
    # input
    A, B, C = map(int, input().split())

    # compute
    max = A + B + C + 9

    # output
    print(max)

=======
Suggestion 7

def main():
    # data load
    a, b, c = map(int, input().split())

    print(10 * max(a, b, c) + a + b + c)
