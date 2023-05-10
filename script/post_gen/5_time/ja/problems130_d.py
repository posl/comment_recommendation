Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    t = 0
    r = 0
    for l in range(N):
        while r < N and t < K:
            t += A[r]
            r += 1
        if t < K:
            break
        ans += N - r + 1
        t -= A[l]
    print(ans)

solve()

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    right = 0
    total = 0
    for left in range(N):
        while right < N and total < K:
            total += A[right]
            right += 1
        if total < K:
            break
        ans += N - right + 1
        if left == right:
            right += 1
        else:
            total -= A[left]
    print(ans)

=======
Suggestion 3

def count_subarray(arr, n, k):
    start = 0
    end = 0
    count = 0
    while end < n:
        while end < n and arr[end] <= k:
            end += 1
        count += (end - start) * (end - start + 1) // 2
        start = end + 1
        end += 1
    return count

n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = count_subarray(a, n, k)
print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    #print(N)
    #print(K)
    #print(A)
    #print(len(A))
    for i in range(N):
        #print("i:" + str(i))
        for j in range(i, N):
            #print("j:" + str(j))
            #print(A[i:j+1])
            if sum(A[i:j+1]) >= K:
                #print("sum:" + str(sum(A[i:j+1])))
                ans += 1
    print(ans)

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    total = 0
    right = 0
    for left in range(N):
        while right < N and total < K:
            total += A[right]
            right += 1
        if total < K:
            break
        ans += N - right + 1
        if left == right:
            right += 1
        else:
            total -= A[left]
    print(ans)

solve()

=======
Suggestion 6

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    sum = 0
    r = 0
    for l in range(N):
        while r < N and sum < K:
            sum += A[r]
            r += 1
        if sum < K:
            break
        ans += N-r+1
        if l == r:
            r += 1
        else:
            sum -= A[l]
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    right = 0
    total = 0

    for left in range(N):
        while right < N and total < K:
            total += A[right]
            right += 1

        if total < K:
            break

        ans += N - right + 1

        if right == left:
            right += 1
        else:
            total -= A[left]

    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    s = 0
    r = 0
    for l in range(n):
        while r < n and s + a[r] < k:
            s += a[r]
            r += 1
        ans += r - l
        if r == l:
            r += 1
        else:
            s -= a[l]
    print(ans)

=======
Suggestion 9

def problem130_d():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    r = 0
    s = 0
    for l in range(n):
        while r < n and s + a[r] < k:
            s += a[r]
            r += 1
        ans += r - l
        if r == l:
            r += 1
        else:
            s -= a[l]
    print(ans)
