def main():
    q = int(input())
    balls = []
    sum = 0
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            balls.append(query[1])
            sum += query[1] * query[2]
        else:
            sum -= balls[0] * query[1]
            balls = balls[query[1]:]
    print(sum)

if __name__ == '__main__':
    main()