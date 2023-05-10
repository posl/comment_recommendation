def solve():
    from heapq import heappush, heappop
    from sys import stdin, stdout
    input = stdin.readline
    print = stdout.write
    q = int(input())
    bag = []
    offset = 0
    for _ in range(q):
        p, *x = map(int, input().split())
        if p == 1:
            heappush(bag, x[0] - offset)
        elif p == 2:
            offset += x[0]
        else:
            print(f'{heappop(bag) + offset}\n')
    return 0
