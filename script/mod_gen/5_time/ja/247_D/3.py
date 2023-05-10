def main():
    q = int(input())
    balls = []
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            for i in range(query[2]):
                balls.append(query[1])
        else:
            sum = 0
            for i in range(query[1]):
                sum += balls[0]
                balls.pop(0)
            print(sum)

if __name__ == '__main__':
    main()