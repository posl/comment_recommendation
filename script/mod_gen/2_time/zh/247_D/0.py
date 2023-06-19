def main():
    q = int(input())
    query = []
    for i in range(q):
        query.append(input().split())
    ball = []
    for i in range(q):
        if query[i][0] == '1':
            for j in range(int(query[i][2])):
                ball.append(int(query[i][1]))
        elif query[i][0] == '2':
            sum = 0
            for j in range(int(query[i][1])):
                sum += ball.pop(0)
            print(sum)

if __name__ == '__main__':
    main()