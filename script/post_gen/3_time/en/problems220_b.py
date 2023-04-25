Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k = int(input())
    a, b = input().split()
    a = int(a, k)
    b = int(b, k)
    print(a*b)

=======
Suggestion 2

def main():
    k = int(input())
    a, b = map(str, input().split())
    a = int(a, k)
    b = int(b, k)
    print(a * b)

=======
Suggestion 3

def main():
    K = int(input())
    A, B = map(str, input().split())
    print(int(A, K) * int(B, K))

=======
Suggestion 4

def main():
    K = int(input())
    A, B = map(str, input().split())

    A = int(A, K)
    B = int(B, K)

    print(A * B)

=======
Suggestion 5

def main():
    k = int(input())
    a, b = map(str, input().split())
    print(int(a, k)*int(b, k))

=======
Suggestion 6

def main():
    k = int(input())
    a, b = map(int, input().split())
    print(a * b)

=======
Suggestion 7

def solve():
    K = int(input())
    A, B = map(int, input().split())
    print(A*B)

=======
Suggestion 8

def solve():
    K = int(input())
    A, B = map(int, input().split())
    print(A*B)

solve()

=======
Suggestion 9

def base_k_to_10(num, k):
    num = str(num)
    return sum([int(i) * (k ** j) for j, i in enumerate(num[::-1])])

k = int(input())
a, b = input().split()
print(base_k_to_10(a, k) * base_k_to_10(b, k))
