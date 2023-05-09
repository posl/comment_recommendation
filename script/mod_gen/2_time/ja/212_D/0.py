def main():
    Q = int(input())
    ball = []
    add = 0
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            ball.append(query[1] - add)
        elif query[0] == 2:
            add += query[1]
        else:
            ball.sort()
            print(ball[0] + add)
            ball.pop(0)

if __name__ == '__main__':
    main()