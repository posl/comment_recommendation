Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            v = sorted(V[:i] + V[N - j:])
            for k in range(min(i + j, K - i - j)):
                if v[k] < 0:
                    v[k] = 0
            ans = max(ans, sum(v))
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N - i, K - i) + 1):
            tmp = V[:i] + V[N - j:]
            tmp.sort()
            ans = max(ans, sum(tmp[K - i - j:]))
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            tmp = V[:i] + V[N - j:]
            tmp.sort()
            for k in range(min(K - i - j, len(tmp))):
                if tmp[k] < 0:
                    tmp[k] = 0
            ans = max(ans, sum(tmp))
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for a in range(min(N, K) + 1):
        for b in range(min(N - a, K - a) + 1):
            if a + b > K:
                continue
            v = V[:a] + V[N - b:]
            v.sort()
            for c in range(min(a + b, K - a - b)):
                if v[c] >= 0:
                    break
                v[c] = 0
            ans = max(ans, sum(v))
    print(ans)

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) + 1):
            if i + j > K:
                continue
            v = V[:i] + V[N - j:]
            v.sort()
            ans = max(ans, sum(v[max(0, i + j - K):]))
    print(ans)

=======
Suggestion 6

def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for left in range(min(N, K) + 1):
        for right in range(min(N, K) - left + 1):
            if left + right > N:
                continue
            tmp = V[:left] + V[N - right:]
            tmp.sort()
            ans = max(ans, sum(tmp[-K:]))
    return ans

print(solve())

import sys

=======
Suggestion 7

def main():
    # Read the input
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    # Solve the problem
    ans = 0
    for a in range(min(N, K) + 1):
        for b in range(min(N - a, K - a) + 1):
            # Try to take out a jewels from the left end and b jewels from the right end
            # The jewels in the middle are left in the cylinder
            # The jewels in your hand are not included in the cylinder
            # You can choose the order of the jewels in your hand
            # The number of jewels in your hand is a + b
            # The values of the jewels in your hand are V_1, ..., V_a, V_{N-b+1}, ..., V_N
            # The values of the jewels in the cylinder are V_{a+1}, ..., V_{N-b}
            # The total value is the sum of the values of the jewels in your hand and the jewels in the cylinder
            # The jewels in the cylinder are in the original order
            # You can choose the order of the jewels in your hand
            # The jewels in your hand are V_1, ..., V_a, V_{N-b+1}, ..., V_N
            # The jewels in the cylinder are V_{a+1}, ..., V_{N-b}
            # The jewels in your hand are V_1, ..., V_a
            # The jewels in the cylinder are V_{a+1}, ..., V_{N-b}, V_{N-b+1}, ..., V_N
            # The jewels in your hand are V_1, ..., V_a, V_{N-b+1}, ..., V_N
            # The jewels in the cylinder are V_{a+1}, ..., V_{N-b}
            # The jewels in your hand are V_1, ..., V_a, V_{N-b+1}, ..., V_N
            # The jewels in the cylinder are V_{a+1}, ..., V_{N-b}
            # The jewels in your hand are V_1, ..., V_a, V_{N-b+1}, ..., V_N
            # The jewels in the cylinder are V_{a+1}, ..., V_{N-b}
            # The jewels in your hand are V_1

=======
Suggestion 8

def solve(N, K, V):
    ans = 0
    for k in range(1, min(K, N)+1):
        for l in range(k+1):
            r = k-l
            tmp = sum(V[:l])+sum(V[N-r:])
            ans = max(ans, tmp+max(0, K-k))
    return ans

=======
Suggestion 9

def read_ints():
    return list(map(int, input().split()))
