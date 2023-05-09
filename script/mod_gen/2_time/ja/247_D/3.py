def main():
    q = int(input())
    balls = []
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            balls.extend([query[1] for i in range(query[2])])
        else:
            print(sum(balls[:query[1]]))
            balls = balls[query[1]:]

if __name__ == '__main__':
    main()