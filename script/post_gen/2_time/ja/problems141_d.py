Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] // (2 ** min(i, M))
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] // 2**M
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i]
        if ans % 2 == 1:
            continue
        if M > 0:
            ans //= 2
            M -= 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    discount = [0] * M
    for i in range(M):
        discount[i] = 2 ** i
    ans = 0
    for i in range(N):
        if A[i] >= discount[M-1]:
            ans += A[i]
        else:
            for j in range(M):
                if A[i] >= discount[j]:
                    ans += A[i] // discount[j]
                    break
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i]
        ans = ans // 2
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    ans = 0
    for i in range(N):
        ans += A[i] * 2 ** min(M, i)
    print(ans - B[N])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        if M == 0:
            break
        if A[i] < 2 ** M:
            A[i] = 0
            M -= 1
        else:
            A[i] -= 2 ** M
            M = 0
    print(sum(A))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = sum(A)
    for i in range(1, N):
        A[i] += A[i-1]
    for i in range(M):
        ans = min(ans, A[-1-i]//2**i)
    print(ans)

=======
Suggestion 9

def main():
    #入力
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    #ソート
    A.sort(reverse=True)
    #割引券の枚数をカウント
    count = [0]*M
    for i in range(M):
        count[i] = count[i-1]+2**i
    #割引券の枚数をカウント
    ans = 0
    for i in range(N):
        for j in range(M):
            if A[i]//count[j] >= 1:
                ans += A[i]//count[j]
                A[i] = A[i]%count[j]
                break
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    print(max(0, A[0] - (A[0] >> M)))
