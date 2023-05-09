def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    Q = int(input())
    d = deque()
    for _ in range(Q):
        query = input().split()
        if query[0] == '1':
            d.append(int(query[1]))
        else:
            c = int(query[1])
            s = 0
            while c > 0:
                x = d.popleft()
                s += x
                c -= 1
            print(s)
