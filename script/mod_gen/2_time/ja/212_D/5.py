def main():
    import sys
    from collections import deque
    from heapq import heappush, heappop
    input = sys.stdin.readline
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    q = deque()
    h = []
    for p, x in query:
        if p == "1":
            q.append(int(x))
        elif p == "2":
            q.append(int(x))
        else:
            while h:
                heappop(h)
            while q:
                heappush(h, q.popleft())
            print(h[0])
    return

if __name__ == '__main__':
    main()