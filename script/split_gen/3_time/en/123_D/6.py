def main():
    import heapq
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    AB = []
    for a in A:
        for b in B:
            AB.append(-a-b)
    heapq.heapify(AB)
    ABC = []
    for i in range(K):
        ab = heapq.heappop(AB)
        for c in C:
            abc = ab - c
            heapq.heappush(ABC, abc)
    for i in range(K):
        print(-heapq.heappop(ABC))
