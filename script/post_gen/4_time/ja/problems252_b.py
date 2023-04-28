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
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(k):
        a[b[i]-1] = 0

    print("Yes" if max(a) > 0 else "No")

main()

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max = 0
    for i in range(N):
        if max < A[i]:
            max = A[i]

    for i in range(K):
        if max == B[i]:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 4

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
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort(reverse=True)
    B.sort()

    for i in range(K):
        if A[i] < B[i]:
            print("Yes")
            exit()

    print("No")
    return

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_a = max(A)
    if max_a in B:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def solve():
    # === 数値を取得 ===
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # === 処理 ===
    # おいしさが最大の食品を取得
    A_max = max(A)

    # 嫌いな食品が含まれているか判定
    for i in range(K):
        if A_max == A[B[i]-1]:
            print("Yes")
            exit()

    # 嫌いな食品が含まれていない場合
    print("No")

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    like = [0] * n
    for i in range(k):
        like[b[i] - 1] = 1
    max = 0
    for i in range(n):
        if like[i] == 0 and max < a[i]:
            max = a[i]
    if max == 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 9

def resolve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for i in range(K):
        if A[0] < A[B[i]-1]:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 10

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    if A[-1] > B[-1]:
        print('Yes')
    else:
        print('No')
