def solve():
    from collections import deque
    q = int(input())
    que = deque()
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            que.appendleft([query[1], query[2]])
        else:
            ans = 0
            for i in range(query[1]):
                a = que.pop()
                ans += a[0]
                a[1] -= 1
                if a[1] != 0:
                    que.append(a)
            print(ans)
solve()
