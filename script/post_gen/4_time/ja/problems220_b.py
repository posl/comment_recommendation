Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k = int(input())
    a, b = input().split()
    a = int(a, k)
    b = int(b, k)
    print(a * b)

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
    k = int(input())
    a, b = input().split()
    print(int(a, k) * int(b, k))

=======
Suggestion 4

def main():
    k = int(input())
    a,b = map(str,input().split())
    print(int(a,k)*int(b,k))

=======
Suggestion 5

def convert_base(num, n):
    if num == 0:
        return '0'
    s = ''
    while num > 0:
        s = str(num % n) + s
        num //= n
    return s

k = int(input())
a, b = map(str, input().split())
a = int(a, k)
b = int(b, k)
print(a * b)

=======
Suggestion 6

def n_to_10(n, k):
    ans = 0
    for i in range(len(n)):
        ans += int(n[i]) * (k ** (len(n)-1-i))
    return ans

k = int(input())
a, b = input().split()
a = n_to_10(a, k)
b = n_to_10(b, k)
print(a*b)

=======
Suggestion 7

def k_to_10(k, n):
    k = int(k)
    n = str(n)
    l = len(n)
    ans = 0
    for i in range(l):
        ans += int(n[i]) * (k ** (l - i - 1))
    return ans

k = input()
a, b = map(str, input().split())

print(k_to_10(k, a) * k_to_10(k, b))
