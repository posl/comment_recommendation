Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    for i in range(N):
        if i == N - 1:
            print(K)
        else:
            if (A[i + 1] - 1) * (i + 1) <= K:
                K -= (A[i + 1] - 1) * (i + 1)
            else:
                print(K // (i + 1) + B[i])
                K = 0

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = [0] + a
    ans = [0] * (N + 1)
    for i in range(N):
        if K >= (a[i + 1] - a[i]) * (i + 1):
            ans[i + 1] = ans[i] + (a[i + 1] - a[i])
            K -= (a[i + 1] - a[i]) * (i + 1)
        else:
            ans[i + 1] = ans[i] + K // (i + 1)
            K = 0
            break
    for i in range(N):
        if K >= N - i:
            ans[i + 1] += N - i
            K -= N - i
        else:
            ans[i + 1] += K
            K = 0
            break
    for i in range(N):
        print(ans[i + 1])

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = [0] + a
    ans = [0] * (N + 1)
    for i in range(N):
        if a[i + 1] - a[i] > 1:
            ans[i + 1] = (a[i + 1] - a[i] - 1) * (i + 1)
    ans = [0] + list(map(int, np.cumsum(ans)))
    for i in range(N):
        if K >= ans[i + 1]:
            continue
        else:
            K -= ans[i]
            break
    if K == 0:
        print(a[i])
    else:
        print(a[i] + 1 + (K - 1) // (i + 1))

=======
Suggestion 5

def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    a = sorted(a)
    ans = [0]*N
    for i in range(N):
        ans[i] = K//(N-i)
        K -= ans[i]
    for i in range(N):
        if K == 0:
            break
        ans[i] += 1
        K -= 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0] * N
    if K >= N:
        ans = [K//N] * N
        K = K % N
    for i in range(K):
        ans[A.index(A[i])] += 1
    print(*ans, sep='

')

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    #print(N, K, a)
    a.sort()
    ans = [0] * N
    #print(a)
    for i in range(N):
        if K <= 0:
            break
        if i == N-1:
            ans[i] += K
            break
        diff = a[i+1] - a[i]
        if K >= diff * (i+1):
            ans[i] += diff
            K -= diff * (i+1)
        else:
            ans[i] += K // (i+1)
            break
    #print(ans)
    for i in range(N):
        ans[i] += K // N
    for i in range(K % N):
        ans[i] += 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.insert(0,0)
    ans = []
    for i in range(N):
        ans.append(K//(N-i))
        K -= K//(N-i)
    for i in range(N):
        if K == 0:
            break
        if a[i+1] - a[i] <= K:
            ans[i] += a[i+1] - a[i]
            K -= a[i+1] - a[i]
        else:
            ans[i] += K
            K = 0
    for i in range(N):
        print(ans[i])

=======
Suggestion 9

def solve(N, K, a):
    a.sort()
    ans = [0] * N
    count = 0
    while K > 0:
        if count == N:
            for i in range(N):
                ans[i] += K // N
            K %= N
        else:
            if K >= N - count:
                K -= N - count
                ans[count] += 1
            else:
                ans[count + K] += 1
                K = 0
        count += 1
    return ans
