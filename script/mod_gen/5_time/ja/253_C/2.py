def main():
    from sys import stdin
    input = stdin.readline
    
    from heapq import heappush, heappop
    
    Q = int(input())
    s = []
    h = []
    for _ in range(Q):
        query = input().split()
        if query[0] == "1":
            x = int(query[1])
            s.append(x)
            heappush(h, x)
        elif query[0] == "2":
            x = int(query[1])
            c = int(query[2])
            for i in range(min(c, s.count(x))):
                s.remove(x)
        else:
            while True:
                if s[0] == h[0]:
                    heappop(h)
                    heappop(s)
                else:
                    break
            print(h[0]-s[0])

if __name__ == '__main__':
    main()