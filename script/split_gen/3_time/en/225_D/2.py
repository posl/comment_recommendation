def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    from collections import deque
    N, Q = map(int, input().split())
    trains = [deque([i]) for i in range(N)]
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            c = trains[q[1]-1].popleft()
            trains[q[2]-1].appendleft(c)
        elif q[0] == 2:
            c = trains[q[1]-1].popleft()
            trains[q[2]-1].pop()
            trains[q[1]-1].appendleft(c)
        else:
            print(len(trains[q[1]-1]), end=' ')
            print(*trains[q[1]-1])
    return
