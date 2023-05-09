def main():
    from collections import deque
    q = int(input())
    que = deque()
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            que.append(query[1])
        elif query[0] == 2:
            sum = 0
            for j in range(query[1]):
                sum += que.popleft()
            print(sum)
