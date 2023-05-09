def main():
    q = int(input())
    balls = []
    sum = 0
    for i in range(q):
        query = input().split()
        if query[0] == "1":
            balls.append(int(query[1]))
            sum = sum + int(query[1])
        else:
            for i in range(int(query[1])):
                sum = sum - balls[0]
                balls.pop(0)
            print(sum)

if __name__ == '__main__':
    main()