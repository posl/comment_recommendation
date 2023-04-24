Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    AB = []
    for i in range(N):
        A, B = map(int, input().split())
        AB.append([A, B])
    AB.sort(key=lambda x: x[0])
    ans = 0
    q = []
    for i in range(M):
        while q and q[0][0] < i:
            heapq.heappop(q)
        while AB and AB[0][0] == i + 1:
            heapq.heappush(q, [-AB[0][1], AB[0][1]])
            AB.pop(0)
        if q:
            ans += heapq.heappop(q)[1]
    print(ans)

=======
Suggestion 2

def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    import heapq
    heap = []
    ans = 0
    for i in range(1, M+1):
        while AB and AB[0][0] == i:
            heapq.heappush(heap, -AB[0][1])
            AB.pop(0)
        if heap:
            ans -= heapq.heappop(heap)
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for i in range(M):
        for j in range(N):
            if AB[j][0] == i + 1:
                ans += AB[j][1]
                AB[j][0] = 0
    print(ans)
main()

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    AB.append([M+1, 0])
    ans = 0
    B = []
    for i in range(N+1):
        if AB[i][0] <= M:
            B.append(AB[i][1])
        else:
            break
    B.sort(reverse=True)
    for i in range(M):
        ans += B[i]
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    B = [0] * (M + 1)
    for i in range(M):
        B[i + 1] = B[i]
        while AB and AB[0][0] == i + 1:
            B[i + 1] = max(B[i + 1], AB[0][1])
            AB.pop(0)
        if i > 0:
            B[i + 1] = max(B[i + 1], B[i])
    print(B[-1])

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(N)]

    AB.sort(key=lambda x: x[0])
    AB.sort(key=lambda x: x[1], reverse=True)
    #print(AB)

    dp = [0] * (M + 1)
    for i in range(M):
        dp[i + 1] = max(dp[i + 1], dp[i])
        for j in range(N):
            if i + AB[j][0] > M:
                continue
            dp[i + AB[j][0]] = max(dp[i + AB[j][0]], dp[i] + AB[j][1])

    print(dp[M])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    que = []
    for i in range(1, M + 1):
        while AB and AB[0][0] == i:
            a, b = AB.pop(0)
            heapq.heappush(que, -b)
        if que:
            ans -= heapq.heappop(que)
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    #print(AB)
    import heapq
    heap = []
    ans = 0
    for i in range(1, M+1):
        while AB and AB[0][0] == i:
            a, b = AB.pop(0)
            heapq.heappush(heap, -b)
        if heap:
            ans -= heapq.heappop(heap)
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    #print(AB)
    ans = 0
    i = 0
    for j in range(1, M+1):
        while i < N and AB[i][0] == j:
            ans += AB[i][1]
            i += 1
        print(ans)
