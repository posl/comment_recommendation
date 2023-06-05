Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def convert_to_decimal(num, base):
    multiplier, result = 1, 0
    while num > 0:
        result += num % 10 * multiplier
        multiplier *= base
        num = num // 10
    return result

=======
Suggestion 2

def main():
    k = int(input())
    a,b = map(int,input().split())
    a = int(str(a),k)
    b = int(str(b),k)
    print(a*b)

=======
Suggestion 3

def main():
    k = int(input())
    a, b = map(int, input().split())
    ans = a * b
    print(ans)

=======
Suggestion 4

def main():
    K = int(input())
    A,B = input().split()
    A = int(A,K)
    B = int(B,K)
    print(A*B)

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
    A = int(A, K)
    B = int(B, K)
    print(A * B)

=======
Suggestion 7

def main():
    k = int(input())
    a, b = map(int, input().split())
    print(a*b)

=======
Suggestion 8

def baseK(n, k):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, k)
        nums.append(str(r))
    return ''.join(reversed(nums))

k = int(input())
a, b = map(int, input().split())
a = baseK(a, k)
b = baseK(b, k)
print(int(a) * int(b))

=======
Suggestion 9

def main():
    k = int(input())
    a, b = map(str, input().split())
    a = int(a, k)
    b = int(b, k)
    print(a*b)
