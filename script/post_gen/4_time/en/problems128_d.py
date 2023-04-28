Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(min(N, K) + 1):
        for r in range(min(N, K) - l + 1):
            if l + r > N:
                break
            t = V[:l] + V[N - r:]
            t.sort()
            for i in range(min(K - l - r, l + r)):
                if t[i] < 0:
                    t[i] = 0
            ans = max(ans, sum(t))
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            l = V[:i] + V[N - j:]
            l.sort()
            ans = max(ans, sum(l[max(K - i - j, 0):]))
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            l = V[:i]
            r = V[N-j:]
            l.sort()
            r.sort()
            for k in range(min(K - i - j, min(i, j))):
                if l[k] < 0 and r[min(K - i - j - k - 1, len(r) - 1)] < 0:
                    l[k], r[min(K - i - j - k - 1, len(r) - 1)] = r[min(K - i - j - k - 1, len(r) - 1)], l[k]
            ans = max(ans, sum(l) + sum(r))
    print(ans)
main()

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(min(N, K) + 1):
        for r in range(min(N, K) - l + 1):
            if l + r > N:
                continue
            tmp = []
            for i in range(l):
                tmp.append(V[i])
            for i in range(r):
                tmp.append(V[N - 1 - i])
            tmp.sort()
            for i in range(min(K - l - r, l + r)):
                if tmp[i] > 0:
                    break
                tmp[i] = 0
            ans = max(ans, sum(tmp))
    print(ans)

solve()

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    for a in range(min(n, k) + 1):
        for b in range(min(n, k) + 1 - a):
            c = k - a - b
            d = v[:a] + v[n-b:]
            d.sort()
            ans = max(ans, sum(d[max(0, c - len(d)):]))
    print(ans)

=======
Suggestion 6

def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(K, N) + 1):
        for j in range(min(K, N) - i + 1):
            left = V[:i]
            right = V[N - j:]
            new = left + right
            new.sort()
            new.reverse()
            for k in range(min(K - i - j, len(new))):
                if new[k] < 0:
                    new[k] = 0
            ans = max(ans, sum(new))
    print(ans)
solve()

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(0, min(N, K) + 1):
        for j in range(0, min(N, K) - i + 1):
            tmp = []
            for k in range(i):
                tmp.append(V[k])
            for k in range(j):
                tmp.append(V[N - k - 1])
            tmp.sort()
            for k in range(min(K - i - j, len(tmp))):
                if tmp[k] < 0:
                    tmp[k] = 0
            ans = max(ans, sum(tmp))
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    max_value = 0
    for left in range(min(N, K) + 1):
        for right in range(min(N, K) + 1 - left):
            values = V[:left] + V[N - right:]
            values.sort()
            for i in range(min(K - left - right, len(values))):
                if values[i] < 0:
                    values[i] = 0
            max_value = max(max_value, sum(values))
    print(max_value)

=======
Suggestion 9

def get_max_sum(N, K, V):
    max_sum = 0
    for i in range(N+1):
        for j in range(N+1):
            if i+j > N:
                continue
            if i+j > K:
                continue
            sum = 0
            l = []
            for k in range(i):
                l.append(V[k])
            for k in range(N-j, N):
                l.append(V[k])
            l.sort()
            for k in range(K-i-j):
                if k < len(l) and l[k] < 0:
                    l[k] = 0
            for k in range(len(l)):
                sum += l[k]
            if sum > max_sum:
                max_sum = sum
    return max_sum

N, K = map(int, input().split())
V = list(map(int, input().split()))
print(get_max_sum(N, K, V))

=======
Suggestion 10

def max_jewels(N, K, V):
    max_sum = 0
    for i in range(1, min(N, K) + 1):
        for j in range(i + 1):
            s = sorted(V[:j] + V[N - (i - j):])
            max_sum = max(max_sum, sum(s[i:]))
    return max_sum
