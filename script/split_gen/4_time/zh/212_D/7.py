def main():
    from sys import stdin
    from heapq import heapify, heappop, heappush
    input = stdin.readline
    q = int(input())
    q1 = []
    q2 = []
    q2_sum = 0
    for _ in range(q):
        p, x = map(int, input().split())
        if p == 1:
            heappush(q1, x)
            q2_sum += x
        elif p == 2:
            heappush(q2, x)
            q2_sum += x
            if len(q2) > len(q1):
                q2_sum -= heappop(q2)
        else:
            print(q1[0], q2_sum)
            if len(q2) > len(q1):
                q2_sum -= heappop(q2)
            heappop(q1)
main()
