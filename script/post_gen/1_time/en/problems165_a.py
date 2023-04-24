Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k = int(input())
    a, b = map(int, input().split())
    for i in range(a, b+1):
        if i % k == 0:
            print("OK")
            return
    print("NG")

=======
Suggestion 2

def main():
    k = int(input())
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        if i % k == 0:
            print("OK")
            break
    else:
        print("NG")

main()

=======
Suggestion 3

def main():
    K = int(input())
    A, B = map(int, input().split())
    for i in range(A, B + 1):
        if i % K == 0:
            print('OK')
            exit()
    print('NG')

=======
Suggestion 4

def main():
    k = int(input())
    a, b = [int(x) for x in input().split()]
    for i in range(a, b+1):
        if i % k == 0:
            print('OK')
            return
    print('NG')

=======
Suggestion 5

def main():
    K = int(input())
    A, B = map(int, input().split())
    if A % K == 0 or B % K == 0 or (A // K + 1) * K <= B:
        print('OK')
    else:
        print('NG')

=======
Suggestion 6

def main():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0 or b % k == 0:
        print("OK")
    elif a // k + 1 <= b // k:
        print("OK")
    else:
        print("NG")

=======
Suggestion 7

def main():
    K = int(input())
    A, B = map(int, input().split())
    if (B // K) - (A // K) >= 1 or A % K == 0:
        print("OK")
    else:
        print("NG")

=======
Suggestion 8

def main():
    k = int(input())
    a, b = map(int, input().split())
    if (b // k) - (a // k) >= 1:
        print("OK")
    else:
        if a % k == 0:
            print("OK")
        else:
            print("NG")

=======
Suggestion 9

def main():
    K = int(input())
    A, B = map(int, input().split())
    if (A % K == 0) or (B % K == 0):
        print('OK')
    else:
        for i in range(A, B+1):
            if i % K == 0:
                print('OK')
                return
        print('NG')

=======
Suggestion 10

def main():
    k = int(input())
    a, b = map(int, input().split())
    if (a % k == 0) or (b % k == 0) or (a < k and k <= b):
        print("OK")
    else:
        print("NG")
