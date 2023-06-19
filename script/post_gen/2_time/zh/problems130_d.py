Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    sumA = [0]*(N+1)
    for i in range(N):
        sumA[i+1] = sumA[i]+A[i]
    ans = 0
    right = 0
    for left in range(N):
        while right < N+1 and sumA[right]-sumA[left] < K:
            right += 1
        ans += N+1-right
    print(ans)

=======
Suggestion 2

def main():
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	
	# a = [6, 1, 2, 7]
	# k = 10
	# n = 4
	# a = [3, 3, 3]
	# k = 5
	# n = 3
	# a = [103, 35322, 232, 342, 21099, 90000, 18843, 9010, 35221, 19352]
	# k = 53462
	# n = 10
	# a = [1, 2, 3, 4, 5]
	# k = 10
	# n = 5
	# a = [1, 2, 3, 4, 5]
	# k = 11
	# n = 5
	# a = [1, 2, 3, 4, 5]
	# k = 5
	# n = 5
	# a = [1, 2, 3, 4, 5]
	# k = 6
	# n = 5
	# a = [1, 2, 3, 4, 5]
	# k = 7
	# n = 5
	# a = [1, 2, 3, 4, 5]
	# k = 8
	# n = 5
	# a = [1, 2, 3, 4, 5]
	# k = 9
	# n = 5
	# a = [1, 2, 3, 4, 5]
	# k = 10
	# n = 5
	# a = [1, 2, 3, 4, 5]
	# k = 11
	# n = 5
	# a = [1, 2, 3, 4, 5]
	# k = 12
	# n = 5
	# a = [1, 2, 3, 4, 5]
	# k = 13
	# n = 5

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(i, N):
            if sum(A[i:j+1]) >= K:
                count += 1
    print(count)

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # print(N, K, A)

    # print('N: ', N)
    # print('K: ', K)
    # print('A: ', A)

    # print('A[0:0]: ', A[0:0])
    # print('A[0:1]: ', A[0:1])
    # print('A[0:2]: ', A[0:2])
    # print('A[0:3]: ', A[0:3])
    # print('A[0:4]: ', A[0:4])
    # print('A[0:5]: ', A[0:5])
    # print('A[0:6]: ', A[0:6])
    # print('A[0:7]: ', A[0:7])
    # print('A[0:8]: ', A[0:8])
    # print('A[0:9]: ', A[0:9])
    # print('A[0:10]: ', A[0:10])
    # print('A[0:11]: ', A[0:11])
    # print('A[0:12]: ', A[0:12])
    # print('A[0:13]: ', A[0:13])
    # print('A[0:14]: ', A[0:14])
    # print('A[0:15]: ', A[0:15])
    # print('A[0:16]: ', A[0:16])
    # print('A[0:17]: ', A[0:17])
    # print('A[0:18]: ', A[0:18])
    # print('A[0:19]: ', A[0:19])
    # print('A[0:20]: ', A[0:20])
    # print('A[0:21]: ', A[0:21])
    # print('A[0:22]: ', A[0:22])
    # print('A[0:23]: ', A[0:23])
    # print('A[0:24]: ', A[0:24])
    # print('A[0:25]: ', A[0

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
        if sum >= K:
            ans += N - right + 1
        sum -= A[left]
    print(ans)
solve()

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    right = 0
    sum = 0
    for left in range(n):
        while right < n and sum < k:
            sum += a[right]
            right += 1
        if sum < k:
            break
        ans += n - right + 1
        if right == left:
            right += 1
        else:
            sum -= a[left]
    print(ans)

=======
Suggestion 7

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    right = 0
    sum = 0
    for left in range(N):
        while right < N and sum + A[right] < K:
            sum += A[right]
            right += 1
        ans += (right - left)
        if right == left:
            right += 1
        else:
            sum -= A[left]
    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    right = 0
    total = 0
    for left in range(n):
        while right < n and total + a[right] < k:
            total += a[right]
            right += 1
        ans += right - left
        if left == right:
            right += 1
        else:
            total -= a[left]
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    #print(N, K)
    #print(a)

    #累積和を求める
    s = [0] * (N+1)
    for i in range(N):
        s[i+1] = s[i] + a[i]
    #print(s)

    #しゃくとり法
    ans = 0
    r = 0
    for l in range(N):
        while r < N+1 and s[r] - s[l] < K:
            r += 1
        ans += N - r + 1
    print(ans)

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = 0
    res = 0
    right = 0
    for left in range(n):
        while right < n and s < k:
            s += a[right]
            right += 1
        if s < k:
            break
        res += n - right + 1
        s -= a[left]
    print(res)
