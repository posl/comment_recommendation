def main():
    from collections import deque
    q = int(input())
    d = deque()
    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            d.append((int(query[1]), int(query[2])))
        else:
            c = int(query[1])
            s = 0
            while c > 0:
                x, y = d.popleft()
                if c >= y:
                    s += x * y
                    c -= y
                else:
                    s += x * c
                    d.appendleft((x, y-c))
                    c = 0
            print(s)
