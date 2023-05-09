def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    q = int(input())
    que = deque()
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            que.appendleft([query[1], query[2]])
        else:
            cnt = query[1]
            ans = 0
            while cnt > 0:
                if que[0][1] > cnt:
                    que[0][1] -= cnt
                    ans += que[0][0] * cnt
                    cnt = 0
                else:
                    ans += que[0][0] * que[0][1]
                    cnt -= que[0][1]
                    que.popleft()
            print(ans)

if __name__ == '__main__':
    main()