Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    maxA = max(A)
    maxB = max(B)

    if maxA > maxB:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    flag = False
    for i in range(N):
        if i + 1 not in B:
            flag = True

    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def read_int():
    return int(input())

=======
Suggestion 4

def problems252_b():
    n = input()
    a = map(int, raw_input().split())
    k = input()
    b = map(int, raw_input().split())
    max_a = max(a)
    for i in b:
        if a[i-1] == max_a:
            print "Yes"
            return
    print "No"

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    maxA = max(A)
    maxB = max(B)

    if maxA > maxB:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for i in range(K):
        A[B[i] - 1] = 0

    print("Yes" if max(A) > 0 else "No")

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if len(set(A) - set(B)) > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    for i in range(k):
        if a[n-1] == b[i]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in range(k):
        a[b[i]-1] = 0
    if max(a) > 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in range(k):
        a[b[i]-1] = 0
    if max(a) == 0:
        print('No')
    else:
        print('Yes')
