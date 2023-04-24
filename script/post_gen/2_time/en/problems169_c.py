Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B = input().split()
    A = int(A)
    B = int(float(B) * 100)
    print(A * B // 100)

=======
Suggestion 2

def main():
    A, B = input().split()
    A = int(A)
    B = float(B)
    print(int(A*B))

=======
Suggestion 3

def main():
    a, b = input().split()
    a = int(a)
    b = float(b)
    print(int(a * b))

=======
Suggestion 4

def main():
    A, B = map(float, input().split())
    print(int(A*B))

=======
Suggestion 5

def main():
    a, b = map(float, input().split())
    print(int(a * b))

=======
Suggestion 6

def main():
    A, B = input().split()
    A = int(A)
    B = int(B.replace('.', ''))
    print(A*B//100)

=======
Suggestion 7

def main():
    a, b = input().split()
    print(int(int(a) * float(b)))

=======
Suggestion 8

def main():
    A, B = input().split()
    print(int(int(A) * float(B)))

=======
Suggestion 9

def main():
    A, B = [x for x in input().split()]
    A = int(A)
    B = int(B.replace('.',''))
    print(A*B//100)

=======
Suggestion 10

def main():
    a, b = input().split()
    a = int(a)
    b = int(b[:2])
    print(a * b // 100)
