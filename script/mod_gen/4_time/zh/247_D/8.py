def main():
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    balls = []
    sum = 0
    for q in query:
        if q[0] == '1':
            balls.extend([int(q[1])] * int(q[2]))
        else:
            for i in range(int(q[1])):
                sum += balls.pop(0)
            print(sum)
            sum = 0

if __name__ == '__main__':
    main()