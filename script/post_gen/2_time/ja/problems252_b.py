Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if max(A) in B:
        print("No")
    else:
        print("Yes")

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(k):
        a[b[i] - 1] = 0
    if sum(a) > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(k):
        if a[0] == a[b[i]-1]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort()
    for i in range(K):
        if A[i] >= B[i]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort(reverse=True)
    B.sort()

    if A[0] > B[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse=True)

    for i in range(k):
        if a[0] == a[b[i] - 1]:
            print('Yes')
            exit()

    print('No')

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    maxA = max(A)
    if maxA in A:
        maxA_index = A.index(maxA)
    else:
        maxA_index = -1
    if maxA_index + 1 in B:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(reverse=True)
    b.sort()
    for i in range(k):
        if a[i] <= b[i]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # おいしい順に並び替え
    A.sort(reverse=True)

    # 嫌いな食品のおいしさを取得
    dislike = [A[b-1] for b in B]

    # おいしい順に並び替え
    dislike.sort(reverse=True)

    # 嫌いな食品の最大値とおいしい順に並び替えた食品の最大値が同じならば嫌いな食品を食べる可能性がある
    if dislike[0] == A[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_a = max(A)
    for i in range(N):
        if A[i] == max_a and (i + 1) not in B:
            print("Yes")
            return
    print("No")
