def main():
    import sys
    input = sys.stdin.readline
    from collections import deque
    q = int(input())
    que = deque()
    for _ in range(q):
        query = list(map(int, input().split()))
        que.append(query)
    que.reverse()
    l = []
    r = []
    for _ in range(q):
        query = que.pop()
        if query[0] == 1:
            l.append(query[1])
            r.append(query[2])
        else:
            ans = 0
            for i in range(len(l)):
                if r[-1] == 0:
                    break
                if l[-1] <= r[-1]:
                    ans += l[-1] * r[-1]
                    r[-1] -= l[-1]
                    l.pop()
                else:
                    ans += r[-1] * r[-1]
                    l[-1] -= r[-1]
                    r.pop()
            print(ans)
