Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0 or b % k == 0 or a // k != b // k:
        print("OK")
    else:
        print("NG")

=======
Suggestion 2

def main():
    k = int(input())
    a,b = map(int,input().split())
    if (a%k == 0) or (b%k == 0):
        print("OK")
    elif (a//k < b//k):
        print("OK")
    else:
        print("NG")

=======
Suggestion 3

def main():
    K = int(input())
    A, B = map(int, input().split())
    if A % K == 0 or B % K == 0 or (A // K < B // K):
        print("OK")
    else:
        print("NG")

main()

=======
Suggestion 4

def main():
    k = int(input())
    a, b = map(int, input().split())
    if a%k == 0 or b%k == 0:
        print('OK')
    elif a//k != b//k:
        print('OK')
    else:
        print('NG')

=======
Suggestion 5

def a165(k,a,b):
    if a%k==0 or b%k==0:
        print('OK')
    elif a//k==b//k:
        print('NG')
    else:
        print('OK')

k=int(input())
a,b=map(int,input().split())
a165(k,a,b)

=======
Suggestion 6

def main():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0 or b % k == 0 or (a // k) != (b // k):
        print('OK')
    else:
        print('NG')

=======
Suggestion 7

def main():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0 or b % k == 0:
        print("OK")
    elif a // k != b // k:
        print("OK")
    else:
        print("NG")

=======
Suggestion 8

def main():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0 or b % k == 0:
        print("OK")
        return
    if a // k != b // k:
        print("OK")
        return
    print("NG")

=======
Suggestion 9

def main():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0:
        print('OK')
    elif b // k > a // k:
        print('OK')
    else:
        print('NG')
