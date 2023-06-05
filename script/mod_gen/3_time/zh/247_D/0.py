def main():
    Q = int(input())
    balls = []
    for _ in range(Q):
        query = input().split()
        if query[0] == '1':
            balls.append((int(query[1]),int(query[2])))
        if query[0] == '2':
            c = int(query[1])
            if len(balls) == c:
                print(sum([i[0] for i in balls]))
                balls = []
            else:
                print(sum([i[0] for i in balls[:c]]))
                balls = balls[c:]

if __name__ == '__main__':
    main()