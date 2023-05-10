Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if M > N:
        print("No")
        return

    A.sort(reverse=True)
    B.sort(reverse=True)

    for i in range(M):
        if A[i] < B[i]:
            print("No")
            return

    print("Yes")

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                b[j] = 0
                break
        else:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if M > N:
        print('No')
        return

    A.sort()
    B.sort()

    for i in range(M):
        if A[i] >= B[i]:
            print('No')
            return

    print('Yes')

main()

=======
Suggestion 4

def check_pasta(pasta, pasta_len):
    for i in range(len(pasta)):
        if pasta[i] == pasta_len:
            return True
    return False

=======
Suggestion 5

def main():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if M > N:
        print("No")
        return

    A.sort()
    B.sort()

    for i in range(M):
        if A[i] >= B[i]:
            print("No")
            return

    print("Yes")

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N < M:
        print("No")
        exit()

    A.sort(reverse=True)
    B.sort(reverse=True)

    for i in range(M):
        if A[i] < B[i]:
            print("No")
            exit()

    print("Yes")

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # N, M = 5, 2
    # A = [1,2,3,4,5]
    # B = [5,5]

    A.sort()
    B.sort()

    if M > N:
        print('No')
        exit()

    if min(A) < min(B):
        print('No')
        exit()

    if max(A) > max(B):
        print('No')
        exit()

    for i in range(M):
        if A[i] >= B[i]:
            print('No')
            exit()

    print('Yes')
    exit()

=======
Suggestion 8

def check(n, m, a, b):
    if n < m:
        return False
    for i in range(m):
        if b[i] not in a:
            return False
    return True

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # aをソートしておく
    a.sort()

    # bをソートしておく
    b.sort()

    # aの最小値とbの最小値を比較
    if a[0] < b[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    if m > n:
        print("No")
    else:
        i = 0
        j = 0
        while i < n and j < m:
            if a[i] <= b[j]:
                i = i + 1
                j = j + 1
            else:
                i = i + 1
        if j == m:
            print("Yes")
        else:
            print("No")
