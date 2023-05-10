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

if __name__ == '__main__':
    solve()