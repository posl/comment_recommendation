Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k = int(input())
    a, b = map(str, input().split())
    print(int(a, k) * int(b, k))

=======
Suggestion 2

def k_to_10(k, num):
    return int(str(num), k)

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
    A, B = input().split()

    A_10 = 0
    B_10 = 0
    for i in range(len(A)):
        A_10 += int(A[i]) * K ** (len(A) - 1 - i)
    for i in range(len(B)):
        B_10 += int(B[i]) * K ** (len(B) - 1 - i)
    print(A_10 * B_10)

=======
Suggestion 5

def main():
    k = int(input())
    a, b = map(str, input().split())
    a = int(a, k)
    b = int(b, k)
    print(a * b)

=======
Suggestion 6

def base_10_to_n(X, n):
    if (int(X/n)):
        return base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

K = int(input())
A, B = map(int, input().split())

A = base_10_to_n(A, 10)
B = base_10_to_n(B, 10)

A = int(A, K)
B = int(B, K)

print(A*B)

=======
Suggestion 7

def main():
    K = int(input())
    A,B = map(str,input().split())
    A = int(A,K)
    B = int(B,K)
    print(A*B)

=======
Suggestion 8

def main():
    K = int(input())
    A, B = map(str, input().split())
    print(int(A, K) * int(B, K))
