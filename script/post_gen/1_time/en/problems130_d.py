Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    r = 0
    s = 0
    for l in range(N):
        while r < N and s < K:
            s += A[r]
            r += 1
        if s >= K:
            ans += N - r + 1
        s -= A[l]
    print(ans)

=======
Suggestion 2

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
        total -= A[left]
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    right = 0
    sum = 0
    for left in range(N):
        while right < N and sum < K:
            sum += A[right]
            right += 1
        if sum >= K:
            ans += N - right + 1
        sum -= A[left]
    print(ans)

main()

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    right = 0
    sum = 0
    for left in range(N):
        while right < N and sum < K:
            sum += A[right]
            right += 1
        if sum >= K:
            ans += N - right + 1
        sum -= A[left]
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sumA = [0] * (N + 1)
    for i in range(N):
        sumA[i + 1] = sumA[i] + A[i]
    ans = 0
    r = 0
    for l in range(N):
        while r < N and sumA[r + 1] - sumA[l] < K:
            r += 1
        if r == N:
            break
        ans += N - r
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(N - i):
            if sum(A[j:j + i + 1]) >= K:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K)
    #print(A)
    ans = 0
    r = 0
    s = 0
    for l in range(N):
        while r < N and s < K:
            s += A[r]
            r += 1
        if s < K:
            break
        ans += N - r + 1
        s -= A[l]
    print(ans)

=======
Suggestion 8

def solve():
    N, K = [int(x) for x in input().split(" ")]
    A = [int(x) for x in input().split(" ")]
    cnt = 0
    r = 0
    s = 0
    for l in range(N):
        while r < N and s < K:
            s += A[r]
            r += 1
        if s >= K:
            cnt += N - r + 1
        s -= A[l]
    return cnt

print(solve())

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    # 2つの累積和を用意
    # 累積和1: A[i]までの累積和
    # 累積和2: A[i]までの累積和 (A[i]がK以上の場合のみ)
    S1 = [0] * (N + 1)
    S2 = [0] * (N + 1)
    for i in range(N):
        S1[i + 1] = S1[i] + A[i]
        if A[i] >= K:
            S2[i + 1] = S2[i] + 1
        else:
            S2[i + 1] = S2[i]
    # S1[i] - S1[j] >= K の場合、S2[i] - S2[j] >= 1 である
    # S2[i] - S2[j] >= 1 の場合、S1[i] - S1[j] >= K である
    # つまり、S1[i] - K >= S1[j] となる S1[j] の個数を求めればよい
    # このとき、S1[i] - K は固定値になる
    # これを二分探索で求める
    for i in range(N + 1):
        # S1[i] - K >= 0 となる最小のjを求める
        l = 0
        r = i
        while r - l > 1:
            m = (l + r) // 2
            if S1[i] - K >= S1[m]:
                l = m
            else:
                r = m
        # S1[i] - K >= S1[l] となるjの個数を求める
        ans += i - l
    print(ans)
