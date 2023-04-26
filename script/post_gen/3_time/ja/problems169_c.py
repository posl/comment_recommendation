Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(float, input().split())
    print(int(a * b))

=======
Suggestion 2

def main():
    a,b = input().split()
    a = int(a)
    b = float(b)
    print(int(a*b))

=======
Suggestion 3

def main():
    a, b = map(float, input().split())
    print(int(a * b // 1))

=======
Suggestion 4

def main():
    a,b = input().split()
    a = int(a)
    b = float(b)
    b = int(b * 100)
    print(a * b // 100)

main()

=======
Suggestion 5

def main():
    A, B = map(float, input().split())
    print(int(A * B // 1))

=======
Suggestion 6

def main():
    A,B = map(str,input().split())
    A = int(A)
    B = int(B.replace(".",""))
    print(A*B//100)

=======
Suggestion 7

def solve():
    a,b = map(float,input().split())
    print(int(a*b))
