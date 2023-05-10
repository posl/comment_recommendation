Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(N+1)
    ans = 0
    for i in range(K):
        ans += A[i]*(A[i+1]-A[i]-1)
    print(ans)

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    #print(N,K,A)
    #print(len(A))
    #print(A[0],A[1])
    #print(A[0:2])
    #print(A[0:3])
    #print(A[0:4])
    #print(A[0:5])
    #print(A[0:6])
    #print(A[0:7])
    #print(A[0:8])
    #print(A[0:9])
    #print(A[0:10])
    #print(A[0:11])
    #print(A[0:12])
    #print(A[0:13])
    #print(A[0:14])
    #print(A[0:15])
    #print(A[0:16])
    #print(A[0:17])
    #print(A[0:18])
    #print(A[0:19])
    #print(A[0:20])
    #print(A[0:21])
    #print(A[0:22])
    #print(A[0:23])
    #print(A[0:24])
    #print(A[0:25])
    #print(A[0:26])
    #print(A[0:27])
    #print(A[0:28])
    #print(A[0:29])
    #print(A[0:30])
    #print(A[0:31])
    #print(A[0:32])
    #print(A[0:33])
    #print(A[0:34])
    #print(A[0:35])
    #print(A[0:36])
    #print(A[0:37])
    #print(A[0:38])
    #print(A[0:39])
    #print(A[0:40])
    #print(A[0:41])
    #print(A[0:42])
    #print(A[0:43])
    #print(A[0:44])
    #print(A[0:45])
    #print(A[0:46])
    #print(A[0:47])
    #print(A[0:48])
    #print(A[0:49])
    #print(A[0:50])
    #print(A[0:51])
    #print(A

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [False] * (N + 1)
    for i in range(N + 1):
        for j in range(K):
            if i - A[j] >= 0 and not dp[i - A[j]]:
                dp[i] = True
    print(sum(dp))

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [False] * (N + 1)
    for i in range(1, N + 1):
        for j in range(K):
            if i - A[j] >= 0 and dp[i - A[j]] == False:
                dp[i] = True
                break
    if dp[N]:
        print('First')
    else:
        print('Second')

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [False]*(n+1)
    for i in range(n+1):
        for j in range(k):
            if i-a[j]>=0:
                dp[i] = dp[i] or not dp[i-a[j]]
    for i in range(n,-1,-1):
        if dp[i]:
            print(i)
            break

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(K):
        if A[i] <= N:
            ans += N % A[i]
            N -= N % A[i]
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(K-1, -1, -1):
        if N >= A[i]:
            ans += (N//A[i]) * A[i]
            N = N%A[i]
    print(ans)

=======
Suggestion 8

def game(N,K,A):
    count = 0
    while N > 0:
        for i in range(K):
            if N >= A[K-i-1]:
                N -= A[K-i-1]
                count += A[K-i-1]
                break
    return count

N,K = map(int,input().split())
A = list(map(int,input().split()))
print(game(N,K,A))

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    dp = [0 for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(K):
            if i - A[j] >= 0 and dp[i-A[j]] == 0:
                dp[i] = 1
    if dp[N] == 1:
        print("First")
    else:
        print("Second")

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = 0
    for i in range(K):
        result = result + A[i] * (N // A[i])
        N = N % A[i]
    print(result)
