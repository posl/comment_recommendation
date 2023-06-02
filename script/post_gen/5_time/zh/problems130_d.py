Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = [0] * (n + 1)
    for i in range(n):
        sum_a[i + 1] = sum_a[i] + a[i]
    ans = 0
    right = 0
    for left in range(n):
        while right < n + 1 and sum_a[right] - sum_a[left] < k:
            right += 1
        ans += n + 1 - right
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]

    ans = 0
    right = 0
    for left in range(n):
        while right < n + 1 and s[right] - s[left] < k:
            right += 1
        ans += n + 1 - right

    print(ans)

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    right = 0
    sum = 0
    for left in range(N):
        while right < N and sum < K:
            sum += A[right]
            right += 1
        if sum < K:
            break
        ans += N - right + 1
        if right == left:
            right += 1
        else:
            sum -= A[left]
    print(ans)

=======
Suggestion 4

def solve(n, k, a):
    ans = 0
    sum = 0
    right = 0
    for left in range(n):
        while (right < n and sum + a[right] < k):
            sum += a[right]
            right += 1
        ans += right - left
        if (right == left):
            right += 1
        else:
            sum -= a[left]
    return ans

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, K, A)
    ans = 0
    sum = 0
    right = 0
    for left in range(N):
        while (right < N and sum < K):
            sum += A[right]
            right += 1
        if (sum < K):
            break
        ans += N - right + 1
        sum -= A[left]
    print(ans)

=======
Suggestion 6

def problems130_d():
    pass

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    right = 0
    sum = 0
    for left in range(N):
        while(right < N and sum < K):
            sum += A[right]
            right += 1
        if sum < K:
            break
        ans += N - right + 1
        if right == left:
            right += 1
        else:
            sum -= A[left]
    print(ans)

=======
Suggestion 8

def solve(n, k, a):
    ans = 0
    s = 0
    right = 0
    for left in range(n):
        while right < n and s + a[right] < k:
            s += a[right]
            right += 1
        ans += right - left
        s -= a[left]
    return ans

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K)
    #print(A)
    #print(A[2:4])
    cnt = 0
    for i in range(N):
        for j in range(i, N):
            #print(A[i:j+1])
            if sum(A[i:j+1]) >= K:
                cnt += 1
    print(cnt)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    cumsum = [0]
    for i in range(N):
        cumsum.append(cumsum[i] + A[i])

    ans = 0

    # しゃくとり法
    r = 0
    for l in range(N):
        while r < N + 1 and cumsum[r] - cumsum[l] < K:
            r += 1

        ans += N - r + 1

    print(ans)
