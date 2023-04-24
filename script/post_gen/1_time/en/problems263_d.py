Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i < N // 2:
            ans += min(L, A[i])
        else:
            ans += min(R, A[i])
    print(ans)

=======
Suggestion 2

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    print(sum(A[:N//2]) * L + sum(A[N//2:]) * R)

=======
Suggestion 3

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    
    A.sort()
    
    ans = 0
    for i in range(N):
        if i < N//2:
            ans += min(A[i], L)
        else:
            ans += min(A[i], R)
            
    print(ans)

=======
Suggestion 4

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    
    ans = 0
    for i in range(N):
        if A[i] < L:
            ans += L
        elif A[i] > R:
            ans += R
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 5

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = A[::-1]
    ans = 0
    for i in range(N):
        if i < N//2:
            ans += min(L, A[i])
        else:
            ans += min(R, A[i])
    print(ans)

=======
Suggestion 6

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A = [max(min(R, a), L) for a in A]
    print(sum(A))

=======
Suggestion 7

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    sum = 0
    for i in range(N//2):
        sum += min(L, A[i])
    for i in range(N//2, N):
        sum += min(R, A[i])
    print(sum)

=======
Suggestion 8

def solve():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = min(max(A[i], L), R)
    print(sum(B))
solve()

=======
Suggestion 9

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()

    #print (A)

    ans = 0
    for i in range(N):
        if A[i] > R:
            ans += (N - i) * R
            break
        elif A[i] < L:
            ans += (N - i) * L
            break
        else:
            ans += A[i]

    print (ans)
