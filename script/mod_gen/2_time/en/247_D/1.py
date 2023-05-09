def main():
    from collections import deque
    q = int(input())
    d = deque()
    sum = 0
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            d.append(query[1])
            sum += query[2]
        else:
            for j in range(query[1]):
                sum -= d.popleft()
            print(sum)

if __name__ == '__main__':
    main()