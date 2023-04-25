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
    b = int(b.replace(".", ""))
    print(a * b // 100)

=======
Suggestion 3

def main():
    A, B = input().split()
    A = int(A)
    B = int(B.replace('.', ''))
    print(A * B // 100)

=======
Suggestion 4

def main():
    a, b = map(float, input().split())
    print(int(a * b))

=======
Suggestion 5

def main():
    a,b = input().split()
    a = int(a)
    b = int(float(b)*100)
    print((a*b)//100)

=======
Suggestion 6

def solve():
    a, b = map(float, input().split())
    print(int(a * b))

=======
Suggestion 7

def problems169_c():
    a, b = input().split()
    a = int(a)
    b = int(float(b)*100)
    print(a*b//100)

=======
Suggestion 8

def main():
    a, b = input().split()
    print(int(float(a) * float(b)))

=======
Suggestion 9

def input_to_list():
    return [int(x) for x in input().split()]
