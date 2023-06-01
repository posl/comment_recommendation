Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_A = max(A)
    max_B = max(B)

    if max_A > max_B:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    n,k = input().split()
    n = int(n)
    k = int(k)
    a = input().split()
    b = input().split()
    a = [int(i) for i in a]
    b = [int(i) for i in b]
    max_a = max(a)
    max_b = max(b)
    if max_a > max_b:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    maxA = max(A)

    for i in range(K):
        if B[i] == A.index(maxA)+1:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 4

def main():
    #输入数据
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    #解决问题
    maxA = max(A)
    maxB = max(B)
    if maxA > maxB:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    for i in range(K):
        A[B[i]-1] = 0
    if max(A) != 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    for i in range(K):
        if A[-1] == B[i]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    foods = list(map(int, input().split()))
    hate_foods = list(map(int, input().split()))
    foods.sort()
    hate_foods.sort()
    for i in range(k):
        if foods[n-1] == hate_foods[i]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    c = [0] * n
    for i in b:
        c[i - 1] = 1

    d = []
    for i in range(n):
        if c[i] == 0:
            d.append(a[i])

    if len(d) == 0:
        print('No')
    else:
        d.sort()
        if d[-1] > a[-1]:
            print('Yes')
        else:
            print('No')

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    i = 0
    j = 0
    while i < N:
        if j < K and A[i] == B[j]:
            j += 1
        else:
            print("Yes")
            return
        i += 1
    print("No")

=======
Suggestion 10

def problems252_b():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in range(k):
        a[b[i]-1] = 0
    print("Yes" if max(a)>0 else "No")
