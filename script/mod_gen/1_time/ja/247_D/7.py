def main():
    from collections import deque
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    ball = deque()
    sum = 0
    for q in range(Q):
        if query[q][0] == 1:
            for _ in range(query[q][2]):
                ball.append(query[q][1])
                sum += query[q][1]
        else:
            for _ in range(query[q][1]):
                sum -= ball.popleft()
            print(sum)

if __name__ == '__main__':
    main()