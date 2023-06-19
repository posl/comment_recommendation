def main():
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    balls = []
    sum = 0
    for q in query:
        if q[0] == 1:
            balls.extend([q[1]] * q[2])
        else:
            for i in range(q[1]):
                sum += balls.pop(0)
            print(sum)
            sum = 0

if __name__ == '__main__':
    main()