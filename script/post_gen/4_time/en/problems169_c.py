Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = input().split()
    a = int(a)
    b = int(float(b) * 100)
    print(a * b // 100)

=======
Suggestion 2

def main():
    a, b = input().split()
    a = int(a)
    b = float(b)
    print(int(a * b))

=======
Suggestion 3

def main():
    A, B = input().split()
    print(int(int(A) * float(B)))

main()

=======
Suggestion 4

def main():
    a, b = map(float, input().split())
    print(int(a * b))

=======
Suggestion 5

def main():
    A, B = map(float, input().split())
    print(int(A * B))

=======
Suggestion 6

def main():
    a, b = input().split()
    print(int(int(a) * float(b)))

=======
Suggestion 7

def main():
    a, b = input().split()
    print(int(a) * int(float(b)))

=======
Suggestion 8

def main():
    a,b = input().split()
    print(int(a)*int(b))

main()

=======
Suggestion 9

def main():
    # read input
    A, B = input().split()

    # compute
    A = int(A)
    B = float(B)
    C = A * B

    # truncate
    C = int(C)

    # print result
    print(C)

main()
