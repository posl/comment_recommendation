def main():
    import heapq
    import sys
    input = sys.stdin.readline
    Q = int(input())
    A = []
    B = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            heapq.heappush(A, query[1])
        elif query[0] == 2:
            B.append(query[1])
        else:
            print(heapq.heappop(A) + sum(B))
            if len(A) == 0:
                A = B
                B = []
            else:
                B = []
    return

if __name__ == '__main__':
    main()