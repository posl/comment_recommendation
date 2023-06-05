def main():
    q = int(input())
    balls = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            balls += [[int(query[1]), int(query[2])]]
        else:
            sum = 0
            for i in range(int(query[1])):
                sum += balls[i][0]
            print(sum)
            balls = balls[int(query[1]):]

if __name__ == '__main__':
    main()