def main():
    import sys
    input = sys.stdin.readline
    from collections import deque
    from bisect import bisect_left
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]
    # print(query)
    box = deque()
    sum_ball = 0
    for i in range(q):
        if query[i][0] == 1:
            box.append(query[i][1])
            sum_ball += query[i][1]
        elif query[i][0] == 2:
            if len(box) >= query[i][1]:
                sum_ball -= sum(box[:query[i][1]])
                for j in range(query[i][1]):
                    box.popleft()
            else:
                print(sum_ball)
                continue
        # print(box, sum_ball)
        print(sum_ball)
