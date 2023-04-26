Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for i in range(K):
        A[B[i]-1] = 0
    if max(A) == 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_A = max(A)
    max_B = max(B)

    if max_A > max_B:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    for i in range(K):
        A[B[i]-1] = 0
    if max(A) > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(k):
        a[b[i]-1] = 0

    if max(a) == 0:
        print('No')
    else:
        print('Yes')

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort()

    for i in range(k):
        if a[i] < b[i]:
            print('Yes')
            return

    print('No')

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    max = 0
    for i in range(0, n):
        if max < a[i]:
            max = a[i]

    for i in range(0, k):
        if max == b[i]:
            print("Yes")
            return

    print("No")

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort(reverse=True)
    b.sort()
    for i in range(k):
        if a[0] == b[i]:
            print('Yes')
            return
    print('No')

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort(reverse=True)

    b_i = 0
    for i in range(n):
        if i == b[b_i]-1:
            b_i += 1
            continue
        else:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    B.reverse()
    for i in range(K):
        if A[N-1] < B[i]:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    #Aの最大値
    max_a = max(A)
    #Bの最小値
    min_b = min(B)

    if max_a > min_b:
        print("Yes")
    else:
        print("No")
