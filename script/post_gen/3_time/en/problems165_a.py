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
    for i in range(A, B + 1):
        if i % K == 0:
            print('OK')
            return
    print('NG')

=======
Suggestion 3

def main():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0 or b % k == 0:
        print("OK")
    elif a // k == b // k:
        print("NG")
    else:
        print("OK")

=======
Suggestion 4

def main():
    # input
    K = int(input())
    A, B = map(int, input().split())

    # compute
    ans = 'NG'
    for i in range(A, B+1):
        if i % K == 0:
            ans = 'OK'
            break

    # output
    print(ans)

=======
Suggestion 5

def main():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0 or b % k == 0 or (a // k) < (b // k):
        print("OK")
    else:
        print("NG")

main()

=======
Suggestion 6

def main():
    k = int(input())
    a, b = map(int, input().split())

    if a % k == 0 or b % k == 0 or (a + k - 1) // k * k <= b:
        print("OK")
    else:
        print("NG")

=======
Suggestion 7

def main():
    K = int(input())
    A, B = map(int, input().split())
    if A % K == 0 or B % K == 0:
        print("OK")
    elif A//K < B//K:
        print("OK")
    else:
        print("NG")

=======
Suggestion 8

def main():
    import math
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0 or b % k == 0:
        print("OK")
    elif math.ceil(a/k) == math.floor(b/k):
        print("OK")
    else:
        print("NG")

=======
Suggestion 9

def is_ok(K,A,B):
    for i in range(A,B+1):
        if i%K==0:
            return True
    return False

=======
Suggestion 10

def main():
    k = int(input()) #k is the multiple that Takahashi the Jumbo wants to achieve
    a, b = map(int, input().split()) #a and b are the range of the carry distance that Takahashi the Jumbo can make
    if a % k == 0 or b % k == 0: #if a or b is a multiple of k
        print('OK') #print OK
    else: #if a and b are not multiples of k
        print('NG') #print NG
