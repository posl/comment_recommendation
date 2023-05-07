def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    Q = int(input())
    que = deque()
    for i in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            for j in range(q[2]):
                que.append(q[1])
        elif q[0] == 2:
            ans = 0
            for j in range(q[1]):
                ans += que.popleft()
            print(ans)
