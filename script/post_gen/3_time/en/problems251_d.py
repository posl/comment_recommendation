Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    W = int(input())
    if W % 2 == 0:
        print(W // 2)
        print(' '.join([str(i) for i in range(1, W // 2 + 1)]))
    else:
        print(W // 2)
        print(' '.join([str(i) for i in range(1, W // 2 + 1)]))

=======
Suggestion 2

def main():
    W = int(input())
    if W%2 == 0:
        print(W//2)
        print(' '.join([str(x) for x in range(1,W//2+1)]))
    else:
        print(W//2+1)
        print(' '.join([str(x) for x in range(1,W//2+2)]))

=======
Suggestion 3

def main():
    w = int(input())
    print(w)
    print(' '.join([str(i) for i in range(1, w + 1)]))

=======
Suggestion 4

def main():
    w = int(input())
    print(w)
    print(" ".join([str(i) for i in range(1, w + 1)]))

=======
Suggestion 5

def main():
    W = int(input())
    print(W)
    print(" ".join([str(i) for i in range(1, W+1)]))

=======
Suggestion 6

def main():
    W = int(input())
    print(W)
    print(' '.join([str(i) for i in range(1, W+1)]))

=======
Suggestion 7

def main():
    w = int(input())
    n = w // 2
    print(n)
    print(' '.join([str(i) for i in range(1, n+1)]))

=======
Suggestion 8

def main():
    W = int(input())
    print(W)
    for i in range(1, W+1):
        print(i, end = " ")

=======
Suggestion 9

def main():
    w = int(input())
    print(w//2)
    for i in range(w//2):
        print(2, end=' ')
    print()

=======
Suggestion 10

def main():
    W = int(input())
    print(W)
    print(*[i for i in range(1, W+1)])

main()

I solved this problem by using the method of generating all combinations of a list. I thought it would be better to use the itertools module, but I didn't know how to use it.
