def main():
    from collections import Counter, deque
    Q = int(input())
    que = [list(map(int, input().split())) for _ in range(Q)]
    c = Counter()
    d = deque()
    for i in range(Q):
        if que[i][0] == 1:
            c[que[i][1]] += 1
            d.append(que[i][1])
        elif que[i][0] == 2:
            if c[que[i][1]] > 0:
                c[que[i][1]] -= 1
                if c[que[i][1]] == 0:
                    c.pop(que[i][1])
                d.append(que[i][1])
        else:
            while d:
                if c[d[0]] > 0:
                    break
                else:
                    d.popleft()
            while d:
                if c[d[-1]] > 0:
                    break
                else:
                    d.pop()
            print(c[d[-1]] - c[d[0]])
