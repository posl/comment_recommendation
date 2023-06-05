Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    for i in range(k):
        a[b[i]-1] = 0
    
    if max(a) > 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print('Yes' if len(set(b) & set(a)) == 0 else 'No')

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print('Yes' if len(set(a) - set(b)) > 0 else 'No')

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(k):
        a[b[i]-1] = 0
    print('Yes' if max(a) > 0 else 'No')

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    if A[-1] > B[-1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max = A[0]
    for i in range(1, N):
        if A[i] > max:
            max = A[i]

    for i in range(K):
        if B[i] == max:
            print("Yes")
            return
    print("No")

=======
Suggestion 8

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

=======
Suggestion 9

def judge_like(food,unlike):
    for i in range(len(unlike)):
        if food == unlike[i]:
            return True
    return False
