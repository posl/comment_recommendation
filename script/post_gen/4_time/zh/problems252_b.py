Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solution(N, K, A, B):
    # 1. 首先找出最大的那个食物
    maxA = max(A)
    # 2. 找出最大的那个食物的索引
    maxAIndex = A.index(maxA)
    # 3. 判断这个索引是否在B中
    if maxAIndex+1 in B:
        return "Yes"
    else:
        return "No"

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    if A[-1] in B:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    x = set(a)
    y = set(b)
    z = x & y
    if len(z) >= 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # N, K = 5, 3
    # A = [6, 8, 10, 7, 10]
    # B = [2, 3, 4]

    # N, K = 5, 2
    # A = [100, 100, 100, 1, 1]
    # B = [5, 4]

    # N, K = 2, 1
    # A = [100, 1]
    # B = [2]

    A.sort()
    B.sort()
    print(A)
    print(B)

    if A[N - K] > B[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

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
Suggestion 6

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    for i in range(K):
        A[B[i]-1] = 0
    if max(A) == 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for i in range(K):
        A[B[i] - 1] = 0

    if max(A) > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(k):
        a[b[i]-1] = 0

    if max(a) == 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 9

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
