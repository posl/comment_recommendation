Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(K):
        ans += A[i]
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if A[i] >= K:
            ans = N - i
            break
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    l = 0
    r = A[-1] + 1
    while r - l > 1:
        mid = (l + r) // 2
        if check(A, mid, K):
            l = mid
        else:
            r = mid
    print(l)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    ans = 0
    for i in range(K):
        ans += A[i]
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    print(A[K-1])

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if N == K:
        print(1)
    else:
        if A[N - K] == A[N - K - 1]:
            print(1)
        else:
            print((A[N - K] - A[N - K - 1]) // (A[N - K - 1] + 1) + 1)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A_list = list(map(int, input().split()))
    A_list.sort(reverse=True)
    print(A_list[K - 1])

=======
Suggestion 8

def  main ():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    print(sum(A[:K]) // K)
