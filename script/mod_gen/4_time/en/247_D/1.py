def main():
    Q = int(input())
    balls = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            balls.append([query[1], query[2]])
        else:
            sum = 0
            for j in range(query[1]):
                sum += balls[j][0]
            print(sum)
            balls = balls[query[1]:]

if __name__ == '__main__':
    main()