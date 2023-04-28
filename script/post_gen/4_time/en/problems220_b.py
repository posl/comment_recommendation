Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    K = int(input())
    A, B = input().split()
    A = int(A, K)
    B = int(B, K)
    print(A * B)

=======
Suggestion 2

def main():
    k = int(input())
    a, b = map(str, input().split())
    a = int(a, k)
    b = int(b, k)
    print(a*b)

=======
Suggestion 3

def main():
    K = int(input())
    A, B = map(str, input().split())
    A = int(A, K)
    B = int(B, K)
    print(A * B)

=======
Suggestion 4

def main():
    k = int(input())
    a, b = map(str, input().split())
    print(int(a, k) * int(b, k))

=======
Suggestion 5

def main():
    k = int(input())
    a, b = input().split()
    print(int(a, k) * int(b, k))

=======
Suggestion 6

def main():
    K = int(input())
    A, B = map(str, input().split())
    print(int(A, K) * int(B, K))

=======
Suggestion 7

def main():
    k = int(input())
    a, b = map(int, input().split())

    a = int(str(a), k)
    b = int(str(b), k)

    print(a * b)

=======
Suggestion 8

def base_k_to_base_10(k, a):
    base_10 = 0
    for i in range(len(a)):
        base_10 += int(a[i]) * pow(k, len(a) - i - 1)
    return base_10

k = int(input())
a, b = map(str, input().split())
a_base_10 = base_k_to_base_10(k, a)
b_base_10 = base_k_to_base_10(k, b)
print(a_base_10 * b_base_10)

=======
Suggestion 9

def calc():
    k = int(input())
    a, b = map(int, input().split())
    print(a*b)

calc()

=======
Suggestion 10

def baseK_to_dec(n, k):
    return int(str(n), k)
