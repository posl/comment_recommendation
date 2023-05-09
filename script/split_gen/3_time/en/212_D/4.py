def main():
    import sys
    from heapq import heappush, heappop
    input = sys.stdin.readline
    
    Q = int(input())
    q = []
    for _ in range(Q):
        p, x = map(int, input().split())
        heappush(q, (p, x))
    
    bag = []
    add = 0
    while q:
        p, x = heappop(q)
        if p == 1:
            heappush(bag, x - add)
        elif p == 2:
            add += x
        else:
            print(heappop(bag) + add)
    
    return
