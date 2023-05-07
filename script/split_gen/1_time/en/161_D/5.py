def solve():
    from collections import deque
    import sys
    input = sys.stdin.readline
    K = int(input())
    q = deque(range(1, 10))
    for i in range(K):
        x = q.popleft()
        if x % 10 > 0:
            q.append(10 * x + x % 10 - 1)
        q.append(10 * x + x % 10)
        if x % 10 < 9:
            q.append(10 * x + x % 10 + 1)
    print(x)
