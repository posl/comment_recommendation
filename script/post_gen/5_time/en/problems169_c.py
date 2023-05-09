Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(str, input().split())
    a = int(a)
    b = int(b.replace('.', ''))
    print(a*b//100)

=======
Suggestion 2

def main():
    a, b = input().split()
    a = int(a)
    b = int(b.replace('.', ''))
    print(a*b//100)

=======
Suggestion 3

def main():
    A, B = map(str, input().split())
    A = int(A)
    B = B.replace('.', '')
    B = int(B)
    ans = A * B // 100
    print(ans)

=======
Suggestion 4

def main():
    a, b = input().split()
    a = int(a)
    b = float(b)
    print(int(a * b))

=======
Suggestion 5

def main():
    a, b = map(float, input().split())
    print(int(a * b))

=======
Suggestion 6

def main():
    # input
    A, B = input().split()
    # compute
    A = int(A)
    B = int(B.replace('.', ''))
    # output
    print(A*B//100)

=======
Suggestion 7

def main():
    a, b = map(float, input().split())
    print(int(a * (b * 100) // 100))

=======
Suggestion 8

def main():
    A, B = input().split()
    print(int(int(A) * float(B)))
