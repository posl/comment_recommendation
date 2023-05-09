def main():
    from collections import deque
    import sys
    readline = sys.stdin.readline
    Q = int(readline())
    S = deque([])
    for _ in range(Q):
        query = list(map(int, readline().split()))
        if query[0] == 1:
            S.append(query[1])
        elif query[0] == 2:
            for _ in range(min(query[2], S.count(query[1]))):
                S.remove(query[1])
        else:
            print(max(S) - min(S))
