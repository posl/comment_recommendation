def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    q = int(input())
    d = deque()
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            d.extend([query[1]]*query[2])
        elif query[0] == 2:
            print(sum(list(d)[:query[1]]))
