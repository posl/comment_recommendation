Synthesizing 10/10 solutions

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
    left = 0
    right = N
    while right - left > 1:
        mid = (left + right) // 2
        if A[mid] < K:
            left = mid
        else:
            right = mid
    if A[left] < K:
        print(N - right)
    else:
        print(N - left)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N):
        if A[i] >= K:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    print(sum(A[:K]) // K)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(sum(a[:k]) // k)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    print(sum(A[0:K]) // K)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    cnt = 0
    for i in range(K):
        cnt += A[i]
    print(cnt)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    print(A[K-1])

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    A.append(0)
    ans = 0
    for i in range(N):
        if A[i] == A[i+1]:
            continue
        else:
            ans += 1
        if ans >= K:
            break
    print(ans)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    print(sum(A[:K]) // K)
