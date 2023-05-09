Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    s = 0
    r = 0
    for l in range(n):
        while r < n and s < k:
            s += a[r]
            r += 1
        if s < k:
            break
        ans += n - r + 1
        s -= a[l]
    print(ans)

solve()

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    s = 0
    r = 0
    for l in range(N):
        while r < N and s < K:
            s += A[r]
            r += 1
        if s < K:
            break
        ans += N - r + 1
        s -= A[l]
    print(ans)
main()

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    sum = 0
    right = 0
    for left in range(N):
        while (right < N and sum < K):
            sum += A[right]
            right += 1
        if sum < K:
            break
        ans += N - right + 1
        sum -= A[left]
    print(ans)

=======
Suggestion 4

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    s = 0
    l = 0
    for r in range(n):
        s += a[r]
        while s >= k:
            ans += n - r
            s -= a[l]
            l += 1
    print(ans)

=======
Suggestion 5

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
        sum -= A[left]
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    right = 0
    s = 0
    for left in range(n):
        while right < n and s + a[right] < k:
            s += a[right]
            right += 1
        ans += right - left
        if right == left:
            right += 1
        else:
            s -= a[left]
    print(ans)

=======
Suggestion 7

def get_contiguous_subsequences(a, k):
    count = 0
    for i in range(len(a)):
        sum = 0
        for j in range(i, len(a)):
            sum += a[j]
            if sum >= k:
                count += 1
                break
    return count

=======
Suggestion 8

def solve(N, K, A):
    # write your code here
    ans = 0
    sum = 0
    left = 0
    for right in range(N):
        sum += A[right]
        while sum >= K:
            ans += N - right
            sum -= A[left]
            left += 1
    return ans

=======
Suggestion 9

def sum_of_contiguous_subsequences(a_list, k):
    result = 0
    for i in range(len(a_list)):
        for j in range(i+1, len(a_list)+1):
            if sum(a_list[i:j]) >= k:
                result += 1
    return result

=======
Suggestion 10

def read_ints():
    return list(map(int, input().split()))
