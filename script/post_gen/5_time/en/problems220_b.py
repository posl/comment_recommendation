Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    K = int(input())
    A, B = input().split()
    A = int(A, K)
    B = int(B, K)
    print(A*B)

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
    a = int(a, k)
    b = int(b, k)
    print(a * b)

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
    print(a * b)

=======
Suggestion 8

def base_k_to_10(n, k):
    res = 0
    for i in range(len(n)):
        res += int(n[i]) * (k ** (len(n)-1-i))
    return res

k = int(input())
a, b = input().split()
print(base_k_to_10(a, k) * base_k_to_10(b, k))
