Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    K = int(input())
    A, B = map(int, input().split())
    for i in range(A, B + 1):
        if i % K == 0:
            print("OK")
            return
    print("NG")

=======
Suggestion 2

def main():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0 or b % k == 0:
        print("OK")
    elif a // k < b // k:
        print("OK")
    else:
        print("NG")

=======
Suggestion 3

def main():
    K = int(input())
    A, B = map(int, input().split())
    if A % K == 0 or B % K == 0:
        print("OK")
    elif A // K != B // K:
        print("OK")
    else:
        print("NG")

=======
Suggestion 4

def main():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0 or (a // k) != (b // k):
        print("OK")
    else:
        print("NG")

=======
Suggestion 5

def main():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0 or b % k == 0:
        print('OK')
    elif b // k - (a - 1) // k > 0:
        print('OK')
    else:
        print('NG')

=======
Suggestion 6

def main():
    k = int(input())
    a,b = map(int,input().split())
    if a % k == 0:
        print("OK")
    elif a // k != b // k:
        print("OK")
    else:
        print("NG")

=======
Suggestion 7

def solve():
    K = int(input())
    A, B = map(int, input().split())
    if A % K == 0 or B % K == 0:
        print("OK")
        return
    if A // K != B // K:
        print("OK")
        return
    print("NG")

=======
Suggestion 8

def is_multiple_of_k(A, B, K):
    for i in range(A, B+1):
        if i % K == 0:
            return True
    return False

K = int(input())
A, B = map(int, input().split())

=======
Suggestion 9

def test():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0 or b % k == 0:
        print('OK')
        return
    for i in range(a, b + 1):
        if i % k == 0:
            print('OK')
            return
    print('NG')

test()

=======
Suggestion 10

def check_multiple_of_k(k, a, b):
    for i in range(a, b+1):
        if i%k == 0:
            return "OK"
    return "NG"
