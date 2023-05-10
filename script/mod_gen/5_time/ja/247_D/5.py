def main():
    from collections import deque
    q = int(input())
    query = deque()
    for i in range(q):
        query.append(list(map(int, input().split())))
    balls = deque()
    for i in range(q):
        if query[i][0] == 1:
            for j in range(query[i][2]):
                balls.append(query[i][1])
        else:
            sum = 0
            for j in range(query[i][1]):
                sum += balls.popleft()
            print(sum)

if __name__ == '__main__':
    main()