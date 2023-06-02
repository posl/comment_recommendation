Synthesizing 10/10 solutions (Duplicates hidden)

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
    if a % k == 0:
        print('OK')
    elif a // k != b // k:
        print('OK')
    else:
        print('NG')

=======
Suggestion 3

def main():
    k = int(input())
    a,b = map(int,input().split())
    if a % k == 0 or b % k == 0:
        print("OK")
    elif a // k != b // k:
        print("OK")
    else:
        print("NG")

=======
Suggestion 4

def main():
    k = int(input())
    a,b = map(int,input().split())
    if a%k == 0:
        print("OK")
    elif b%k == 0:
        print("OK")
    else:
        print("NG")

=======
Suggestion 5

def main():
    K = int(input())
    A, B = map(int, input().split())
    if A%K == 0 or B%K == 0:
        print('OK')
    elif A//K != B//K:
        print('OK')
    else:
        print('NG')

=======
Suggestion 6

def main():
    # input
    k = int(input())
    a, b = map(int, input().split())

    # check
    if b // k * k >= a:
        print("OK")
    else:
        print("NG")

=======
Suggestion 7

def main():
    k = int(input())
    a, b = map(int, input().split())
    for i in range(a, b+1):
        if i % k == 0:
            print("OK")
            exit()
    print("NG")

=======
Suggestion 8

def isKMultiple(K, A, B):
    if A <= K and K <= B:
        return True
    else:
        return False
