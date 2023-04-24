Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if B == 1:
        print(0)
    else:
        print((B - 2) // (A - 1) + 1)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print((B + A - 3) // (A - 1))

=======
Suggestion 3

def main():
    A, B = map(int, input().split())

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if B == 1:
        print(0)
    else:
        print((B+A-3)//(A-1))

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print((b + a - 1) // a)

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    print((B-1) // (A-1))

=======
Suggestion 7

def  main():
    a, b = map(int, input().split())
    print((b - 1 + a - 1) // (a - 1))

=======
Suggestion 8

def main():
    A,B = input().split()
    A = int(A)
    B = int(B)
    count = 1
    while(A*B > A):
        A = A*B
        count = count + 1
    print(count)

main()
