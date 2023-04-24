Synthesizing 10/10 solutions (Duplicates hidden)

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
    k = int(input())
    a, b = input().split()
    print(int(a, k) * int(b, k))

=======
Suggestion 4

def main():
    K = int(input())
    A, B = map(str, input().split())
    print(int(A, K) * int(B, K))

=======
Suggestion 5

def main():
    k = int(input())
    a, b = map(int, input().split())
    print(a * b)

=======
Suggestion 6

def main():
    # K = int(input())
    # A, B = map(int, input().split())
    K = 7
    A, B = 123, 456

    A = str(A)
    B = str(B)

    A10 = 0
    B10 = 0
    for i in range(len(A)):
        A10 += int(A[len(A) - i - 1]) * (K ** i)
    for i in range(len(B)):
        B10 += int(B[len(B) - i - 1]) * (K ** i)

    print(A10 * B10)

=======
Suggestion 7

def convert_to_decimal(number, base):
    number = str(number)
    number = number[::-1]
    decimal = 0
    for i in range(len(number)):
        decimal += int(number[i]) * (base ** i)
    return decimal

=======
Suggestion 8

def solve(K, A, B):
    a = int(A, K)
    b = int(B, K)
    return a * b

=======
Suggestion 9

def base_k_to_decimal(x, k):
    x = str(x)
    k = int(k)
    result = 0
    for i in range(len(x)):
        result += int(x[i])*(k**(len(x)-i-1))
    return result
