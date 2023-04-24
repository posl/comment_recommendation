Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = [-1] * n
    for i in range(n):
        p[i] -= 1
    for i in range(n):
        if ans[i] != -1:
            continue
        j = i
        while True:
            ans[j] = i + 1
            j = p[j]
            if ans[j] != -1:
                break
    for i in range(n):
        print(ans[i])

=======
Suggestion 2

def main():
    import sys
    from collections import deque
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    N, K = map(int, readline().split())
    P = list(map(int, readline().split()))
    P = [p-1 for p in P]
    D = deque(P)
    ans = [-1]*N
    for i in range(N):
        p = D.popleft()
        ans[p] = i+1
        if i+1 >= K:
            break
    for i in range(N):
        p = P[i]
        if ans[p] == -1:
            ans[p] = ans[D[0]] + K
    print(*ans, sep='

')

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    cards = [0] * N
    for i in range(N):
        cards[i] = i + 1
    for i in range(N):
        cards[P[i] - 1] = i + 1
    print(cards)
    result = [-1] * N
    stack = []
    for i in range(N):
        stack.append(cards[i])
        if len(stack) >= K:
            for j in range(K):
                result[stack.pop() - 1] = i + 1
    for i in range(N):
        print(result[i])

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = [-1] * N
    stack = []
    for i in range(N):
        p = P[i]
        while stack and stack[-1][0] < p:
            stack.pop()
        stack.append((p, i))
        if len(stack) == K:
            ans[stack[0][1]] = i + 1
            stack = stack[1:]
    for i in range(N):
        p = P[i]
        if ans[p - 1] == -1:
            ans[p - 1] = N
    print('

'.join(list(map(str, ans))))

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    # N, K = map(int, input().split())
    # P = list(map(int, input().split()))
    P = [x - 1 for x in P]
    # print(P)
    # print(N, K)
    # print(P)
    # P = [2, 4, 0, 1, 3]
    # N = 5
    # K = 2
    # P = [2, 4, 0, 1, 3]
    # N = 5
    # K = 1
    # P = [2, 4, 0, 1, 3]
    # N = 5
    # K = 3
    # P = [2, 4, 0, 1, 3]
    # N = 15
    # K = 3
    # P = [2, 13, 14, 8, 1, 5, 4, 12, 0, 6, 9, 10, 7, 11, 3]
    # N = 15
    # K = 1
    # P = [2, 13, 14, 8, 1, 5, 4, 12, 0, 6, 9, 10, 7, 11, 3]
    # N = 15
    # K = 2
    # P = [2, 13, 14, 8, 1, 5, 4, 12, 0, 6, 9, 10, 7, 11, 3]
    # N = 15
    # K = 3
    # P = [2, 13, 14, 8, 1, 5, 4, 12, 0, 6, 9, 10, 7, 11, 3]
    # N = 15
    # K = 4
    # P = [2, 13, 14, 8, 1, 5, 4, 12, 0, 6, 9

=======
Suggestion 6

def main():
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = [-1] * N
    stack = []
    for i in range(N):
        while stack and stack[-1][0] < P[i]:
            ans[stack.pop()[1]] = i + 1
        stack.append((P[i], i))
    while stack:
        ans[stack.pop()[1]] = N + K
    for i in range(N):
        print(ans[i])

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [i - 1 for i in P]
    eaten = [-1] * N
    for i in range(N):
        if eaten[i] != -1:
            continue
        eaten[i] = i
        j = i
        while True:
            j = P[j]
            if eaten[j] != -1:
                break
            eaten[j] = i
    for i in range(N):
        if eaten[i] == -1:
            continue
        j = i
        while True:
            j = P[j]
            if eaten[j] == i:
                break
            eaten[j] = i
    for i in range(N):
        print(eaten[i] + 1)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    K = min(K, N - K)
    ans = [-1] * N
    for i in range(N):
        if ans[i] == -1:
            j = i
            cnt = 0
            while ans[j] == -1:
                ans[j] = i + 1
                j = P[j] - 1
                cnt += 1
            if cnt > K:
                for l in range(N):
                    if ans[l] == i + 1:
                        ans[l] = -1
    print(*ans, sep = "

")

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = [-1 for _ in range(N)]
    #print(N, K, P)
    #print(ans)
    table = []
    for i, p in enumerate(P):
        table.append(p)
        while len(table) >= K:
            #print(table)
            if table[-K] == min(table[-K:]):
                for j in range(K):
                    ans[table.pop() - 1] = i + 1
            else:
                break
    print('

'.join(map(str, ans)))

main()

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    # init
    tbl = [0] * (N + 1)
    for i in range(N):
        tbl[P[i]] = i
    # solve
    ans = [-1] * N
    for x in range(1, N + 1):
        if ans[x - 1] >= 0:
            continue
        # x is not eaten
        i = tbl[x]
        for j in range(i, i + K):
            if j >= N:
                break
            ans[P[j] - 1] = x
    # output
    for i in range(N):
        print(ans[i])
