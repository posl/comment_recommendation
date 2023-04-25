Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    for i in range(min(n, k) + 1):
        for j in range(min(n, k) - i + 1):
            l = v[:i] + v[n - j:]
            l.sort()
            ans = max(ans, sum(l[max(0, k - i - j):]))
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))

    ans = 0
    for i in range(min(N, K)+1):
        for j in range(min(N, K)-i+1):
            if i+j > N:
                continue
            l = V[:i]
            r = V[N-j:]
            l.sort()
            r.sort()
            s = sum(l)
            s += sum(r)
            for k in range(min(K-i-j, i+j)):
                if l[k] < 0:
                    s -= l[k]
            ans = max(ans, s)
    print(ans)

main()

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    result = 0
    for i in range(min(N, K)+1):
        for j in range(min(N, K)-i+1):
            jewels = V[:i] + V[N-j:]
            jewels.sort()
            for k in range(min(len(jewels), K-i-j)):
                if jewels[k] < 0:
                    jewels[k] = 0
            result = max(result, sum(jewels))
    print(result)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    max_sum = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            jewels = V[:i] + V[N - j:]
            jewels.sort()
            sum_jewels = sum(jewels)
            for k in range(min(K - i - j, i + j)):
                if jewels[k] < 0:
                    sum_jewels -= jewels[k]
            if sum_jewels > max_sum:
                max_sum = sum_jewels
    print(max_sum)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    max_value = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            values = V[:i] + V[N-j:]
            values.sort()
            value = sum(values)
            for k in range(min(K-i-j, len(values))):
                if values[k] < 0:
                    value -= values[k]
            max_value = max(max_value, value)
    print(max_value)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    result = 0
    for i in range(1, min(N, K)+1):
        for j in range(i+1):
            jewels = V[:j] + V[N-(i-j):]
            jewels.sort()
            for k in range(min(K-i, len(jewels))):
                if jewels[k] < 0:
                    jewels[k] = 0
            result = max(result, sum(jewels))
    print(result)

=======
Suggestion 7

def problem():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0

    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            jewels = V[:i] + V[N-j:]
            jewels.sort()
            for k in range(min(K-i-j, len(jewels))):
                if jewels[k] < 0:
                    jewels[k] = 0
            ans = max(ans, sum(jewels))

    print(ans)

problem()

=======
Suggestion 8

def max_sum(N, K, V):
    result = 0
    for i in range(1, min(N, K)+1):
        for j in range(i+1):
            left = V[:j]
            right = V[N-(i-j):]
            left.sort()
            right.sort()
            for k in range(min(K-i, j)):
                if left[k] < 0:
                    left[k] = 0
            for k in range(min(K-i, i-j)):
                if right[k] < 0:
                    right[k] = 0
            result = max(result, sum(left)+sum(right))
    return result

=======
Suggestion 9

def solve(n,k,v):
    ans = 0
    for i in range(min(n,k)+1):
        for j in range(min(n,k)-i+1):
            if i+j > n:
                continue
            t = v[:i] + v[n-j:]
            t.sort()
            ans = max(ans, sum(t[max(0,k-i-j):]))
    return ans

=======
Suggestion 10

def max_jewel_value(N, K, V):
    max_value = 0
    for i in range(min(K, N)+1):
        for j in range(min(K-i, N-i)+1):
            if i+j > N:
                break
            temp = V[:i] + V[N-j:]
            temp.sort()
            for k in range(min(K-i-j, len(temp))):
                if temp[k] < 0:
                    temp[k] = 0
            max_value = max(max_value, sum(temp))
    return max_value
