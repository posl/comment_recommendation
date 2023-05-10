Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    if A[-1] > B[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in B:
        A[i-1] = -1
    print("Yes" if max(A) > 0 else "No")

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    for i in range(N):
        if i+1 in B:
            A[i] = 0
    if max(A) == 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for i in range(K):
        A[B[i] - 1] = 0

    if max(A) == 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort(reverse=True)

    for i in range(k):
        if a[i] > b[i]:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort(reverse=True)
    B.sort(reverse=True)

    for i in range(K):
        if A[i] > B[i]:
            print("Yes")
            exit()

    print("No")

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    #print(n, k)
    #print(a)
    #print(b)

    #print(max(a))

    #print(max(b))

    if max(a) > max(b):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in b:
        if a[i-1] == max(a):
            print("Yes")
            exit()
    print("No")

=======
Suggestion 9

def main():
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
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for i in range(K):
        A[B[i] - 1] = 0
    if max(A) > 0:
        print('Yes')
    else:
        print('No')
