Synthesizing 10/10 solutions (Duplicates hidden)

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

    for i in range(a, b+1):
        if i % k == 0:
            print("OK")
            exit()

    print("NG")

=======
Suggestion 3

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
Suggestion 4

def main():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0 or b % k == 0:
        print("OK")
        return
    for i in range(a, b+1):
        if i % k == 0:
            print("OK")
            return
    print("NG")
    return

=======
Suggestion 5

def main():
    k = int(input())
    a, b = map(int, input().split())
    if b // k * k >= a:
        print("OK")
    else:
        print("NG")

=======
Suggestion 6

def main():
    k = int(input())
    a,b = map(int, input().split())
    if a % k == 0 or b % k == 0:
        print("OK")
    elif a // k < b // k:
        print("OK")
    else:
        print("NG")

=======
Suggestion 7

def main():
    k = int(input())
    a, b = map(int, input().split())
    if b//k >= a//k:
        print("OK")
    else:
        print("NG")

=======
Suggestion 8

def main():
    k = int(input())
    a, b = map(int, input().split())
    if a <= b and a % k == 0:
        print("OK")
    else:
        print("NG")

=======
Suggestion 9

def main():
    K = int(input())
    A, B = map(int, input().split())
    if A % K == 0 or B % K == 0:
        print("OK")
        exit()
    else:
        print("NG")
        exit()
