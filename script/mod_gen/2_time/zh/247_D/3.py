def main():
    Q = int(input())
    ball = []
    sum = 0
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            for i in range(int(query[2])):
                ball.append(int(query[1]))
        else:
            for i in range(int(query[1])):
                sum += ball[0]
                del ball[0]
            print(sum)
            sum = 0

if __name__ == '__main__':
    main()