def solve():
    from collections import deque
    Q = int(input())
    que = deque()
    s = 0
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            que.append(query[2])
            s += query[1] * query[2]
        else:
            while query[1] > 0:
                if query[1] >= que[0]:
                    query[1] -= que[0]
                    s -= que[0] * que.popleft()
                else:
                    s -= query[1] * que[0]
                    que[0] -= query[1]
                    query[1] = 0
        if query[0] == 2:
            print(s)
