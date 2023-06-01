Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = input().split()
    a = int(a)
    b = int(b)
    if 0 <= a and b <= 1000:
        print((a * b) / 100)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print(a*b/100)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    print(A * B / 100)

=======
Suggestion 4

def main():
    A, B = input().split()
    A = int(A)
    B = int(B)
    print(A * B / 100)

=======
Suggestion 5

def calculate_energy(a, b):
    return a * b / 100
