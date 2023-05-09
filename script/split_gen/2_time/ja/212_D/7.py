def main():
    import heapq
    import sys
    input = sys.stdin.readline
    q = int(input())
    # ヒープキューを用いて、最小値を常に取り出せるようにする
    q1 = []
    # 今までの操作の合計値を保持する
    s = 0
    for _ in range(q):
        p, *x = map(int, input().split())
        if p == 1:
            heapq.heappush(q1, x[0] - s)
        elif p == 2:
            s += x[0]
        else:
            print(heapq.heappop(q1) + s)
