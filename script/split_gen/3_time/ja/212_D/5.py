def main():
    import sys
    input = sys.stdin.readline
    from heapq import heappop, heappush
    # 1行目
    Q = int(input())
    # 2行目以降
    query = [list(map(int, input().split())) for _ in range(Q)]
    #print(query)
    #print("Q", Q)
    #print("quer
