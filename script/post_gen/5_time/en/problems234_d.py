Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = []
    for i in range(N-K+1):
        ans.append(sorted(P[i:i+K])[-1])
    for i in ans:
        print(i)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    for i in range(N-K+1):
        print(sorted(P[i:i+K])[-1])

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = []
    for i in range(n-k+1):
        ans.append(max(p[i:i+k]))
    print('\n'.join(map(str, ans)))

=======
Suggestion 4

def get_input():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    return n, k, p

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    ans = []
    for i in range(k, n+1):
        ans.append(sorted(p[:i])[k-1])

    for a in ans:
        print(a)

=======
Suggestion 6

def main():
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    for i in range(N-K+1):
        print(sorted(P[i:i+K])[K-1])

=======
Suggestion 7

def problems234_d():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    L = [0] * N
    for i in range(N):
        L[P[i] - 1] = i
    ans = []
    for i in range(K - 1, N):
        ans.append(L[i])
    ans.sort()
    for i in range(len(ans)):
        print(ans[i] + 1)

problems234_d()

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    import heapq
    heap = []
    for i in range(n):
        heapq.heappush(heap, p[i])
        if i >= k-1:
            print(heapq.nlargest(k, heap)[-1])

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    p2 = [0] * (n+1)
    for i in range(1, n+1):
        p2[i] = p2[i-1] + p[i]
    for i in range(k, n+1):
        print(p2[i] - p2[i-k])

=======
Suggestion 10

def solve():
    N, K = list(map(int, input().split()))
    P = list(map(int, input().split()))
    # print(N, K, P)
    from collections import deque
    queue = deque()
    queue.append(P[0])
    for i in range(1, K):
        while len(queue) > 0 and queue[-1] < P[i]:
            queue.pop()
        queue.append(P[i])
    # print(queue)
    print(queue[0])
    for i in range(K, N):
        if queue[0] == P[i-K]:
            queue.popleft()
        while len(queue) > 0 and queue[-1] < P[i]:
            queue.pop()
        queue.append(P[i])
        # print(queue)
        print(queue[0])
