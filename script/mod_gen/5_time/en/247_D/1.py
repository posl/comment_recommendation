def main():
    q = int(input())
    balls = []
    sum = 0
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            balls.append(int(query[1]))
            sum += int(query[2])
        else:
            print(sum)
            sum -= sum(balls[:int(query[1])])
            del balls[:int(query[1])]

if __name__ == '__main__':
    main()