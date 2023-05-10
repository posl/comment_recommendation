Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    B = []
    for i in range(N-1):
        B.append(A[i+1] - A[i])

    B.sort()

    ans = 0
    for i in range(N-K):
        ans += B[i]

    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    if N == K:
        print("Yes")
        return

    if K == 1:
        if A == sorted(A):
            print("Yes")
        else:
            print("No")
        return

    if K % 2 == 0:
        if A == sorted(A):
            print("Yes")
        else:
            print("No")
        return

    if N % 2 == 0:
        if A == sorted(A):
            print("Yes")
        else:
            print("No")
        return

    if A == sorted(A):
        print("Yes")
    else:
        print("No")
    return

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = A[K-1::]
    if A[K-1] == A[-1]:
        print("No")
        return
    if K == 1:
        print("Yes")
        return
    if len(B) == len(set(B)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(N-K):
        if a[i] > a[i+K]:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n-k):
        if a[i] < a[i+k]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A_sorted = sorted(A)
    for i in range(N-K):
        if A_sorted[i] != A_sorted[i+K]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    # データ入力
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # データ整理
    A.sort()
    # 並び替え可能かどうかの判定
    for i in range(N-K):
        if A[i] == A[i+K]:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N - K):
        if A[i] == A[i + K]:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 9

def check(a, k):
    for i in range(len(a) - k):
        if a[i] > a[i + k]:
            return False
    return True

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = A[::-1]
    for i in range(N-K):
        if A[i] == B[i]:
            print("Yes")
            exit()
    print("No")
