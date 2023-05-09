Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = (N-1) // (K-1)
    if (N-1) % (K-1) != 0:
        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-k):
        if a[i] < a[i+k]:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    if (N - 1) % (K - 1) == 0:
        ans = (N - 1) // (K - 1)
    else:
        ans = (N - 1) // (K - 1) + 1
    print(ans)

=======
Suggestion 4

def problems101_c():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N-K):
        if A[i] < A[i+K]:
            print('Yes')
        else:
            print('No')

=======
Suggestion 5

def problems101_c():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-K):
        if A[i] < A[i+K]:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 1
    if (n-1)%(k-1) != 0:
        ans += 1
    ans += (n-1)//(k-1)
    print(ans)

=======
Suggestion 7

def main():
    #n, k = map(int, input().split())
    #a = list(map(int, input().split()))
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    #n = int(input())
    #a = list(map(int, input().split()))

    count = 0
    while n > 0:
        n -= k-1
        count += 1
    print(count)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = 0
    for i in range(1, N):
        if (N - i) % (K - 1) == 1:
            result += 1
    print(result)

=======
Suggestion 9

def min_operations(N, K, A):
    count = 0
    for i in range(0, N, K-1):
        count += 1
    return count

=======
Suggestion 10

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    minnum = min(A)
    minnum_index = A.index(minnum)
    print(int((N-1)/(K-1)) if (N-1)%(K-1)==0 else int((N-1)/(K-1))+1)
