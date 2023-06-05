Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0 or b % k == 0:
        print('OK')
    elif a // k != b // k:
        print('OK')
    else:
        print('NG')

=======
Suggestion 2

def main():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0 or b % k == 0:
        print('OK')
    elif k <= b - a:
        print('OK')
    else:
        print('NG')

=======
Suggestion 3

def main():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0 or b % k == 0:
        print('OK')
    elif a // k == b // k:
        print('NG')
    else:
        print('OK')

=======
Suggestion 4

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
Suggestion 5

def main():
    # input
    k = int(input())
    a, b = map(int, input().split())
    # output
    if a % k == 0 or b % k == 0:
        print("OK")
    elif a // k == b // k:
        print("NG")
    else:
        print("OK")

=======
Suggestion 6

def main():
    # input
    k = int(input())
    a, b = map(int, input().split())

    # output
    if a % k == 0 or b % k == 0:
        print("OK")
    elif a // k != b // k:
        print("OK")
    else:
        print("NG")

=======
Suggestion 7

def main():
    k = int(input())
    a, b = map(int, input().split())
    if (b//k)-(a-1)//k >= 1:
        print("OK")
    else:
        print("NG")

=======
Suggestion 8

def main():
    k = int(input())
    a, b = map(int, input().split())
    for i in range(a, b+1):
        if i % k == 0:
            print("OK")
            return
    print("NG")

=======
Suggestion 9

def main():
    k=int(input())
    a,b=map(int,input().split())
    if a%k==0 or b%k==0:
        print("OK")
    elif a//k!=b//k:
        print("OK")
    else:
        print("NG")

=======
Suggestion 10

def solve():
    #K = int(input())
    #A, B = map(int, input().split())
    K = 7
    A = 500
    B = 600
    if K % A == 0 or K % B == 0:
        print("OK")
    else:
        print("NG")
