Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = input().split()
    a = int(a)
    b = int(b.replace('.', ''))
    print(a * b // 100)

=======
Suggestion 2

def main():
    A, B = input().split()
    A = int(A)
    B = int(float(B) * 100)
    print(A * B // 100)

=======
Suggestion 3

def main():
    a, b = input().split()
    a = int(a)
    b = int(b.replace(".", ""))
    print(a * b // 100)

=======
Suggestion 4

def main():
    A, B = input().split()
    A = int(A)
    B = int(B.replace(".", ""))
    print(A * B // 100)

=======
Suggestion 5

def main():
    A, B = map(str, input().split())
    A = int(A)
    B = int(float(B) * 100)

    print((A * B) // 100)

=======
Suggestion 6

def main():
    A, B = input().split()
    A = int(A)
    B = int(float(B)*100)
    print((A*B)//100)

=======
Suggestion 7

def compute():
    a,b = input().split()
    a = int(a)
    b = int(b.replace('.',''))
    print(a*b//100)

compute()

=======
Suggestion 8

def main():
    a,b = map(float,input().split())
    print(int(a*b//1))

=======
Suggestion 9

def main():
    A,B = map(float,input().split())
    print(int(A*B//1))

=======
Suggestion 10

def multiply(a, b):
    return int(a * b)
