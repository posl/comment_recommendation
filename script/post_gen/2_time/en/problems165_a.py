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
    K = int(input())
    A, B = map(int, input().split())
    for i in range(A, B+1):
        if i % K == 0:
            print("OK")
            return
    print("NG")

=======
Suggestion 3

def main():
    k = int(input())
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        if i % k == 0:
            print("OK")
            exit()
    print("NG")

=======
Suggestion 4

def main():
    K = int(input())
    A, B = map(int, input().split())
    for i in range(A, B+1):
        if i % K == 0:
            print('OK')
            exit()
    print('NG')

=======
Suggestion 5

def main():
    K = int(input())
    A, B = map(int, input().split())
    if A % K == 0:
        print("OK")
    elif B % K == 0:
        print("OK")
    elif A < K and B < K:
        print("NG")
    elif A < K and B > K:
        print("OK")
    elif A > K and B < K:
        print("NG")
    elif A > K and B > K:
        if (A // K) < (B // K):
            print("OK")
        else:
            print("NG")

main()

=======
Suggestion 6

def main():
    K = int(input())
    A, B = map(int, input().split())
    if A % K == 0:
        print("OK")
    elif B % K == 0:
        print("OK")
    elif A // K < B // K:
        print("OK")
    else:
        print("NG")

=======
Suggestion 7

def main():
    k = int(input())
    a, b = map(int, input().split())
    if b // k - a // k >= 1:
        print("OK")
    else:
        print("NG")

=======
Suggestion 8

def main():
    #input
    K = int(input())
    A, B = map(int, input().split())
    #compute
    for i in range(A, B+1):
        if i%K == 0:
            print("OK")
            break
    else:
        print("NG")

=======
Suggestion 9

def main():
    k = int(input())
    a, b = map(int, input().split())
    print("OK" if (b // k - (a - 1) // k) > 0 else "NG")

=======
Suggestion 10

def main():
    # Get the input
    k = int(input())
    a, b = map(int, input().split())
    # Check the condition
    if a % k == 0 or b % k == 0 or (a // k + 1) * k <= b:
        print('OK')
    else:
        print('NG')
