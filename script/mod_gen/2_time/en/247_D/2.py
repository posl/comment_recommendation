def main():
    q = int(input())
    balls = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            balls.append(int(query[1]))
        else:
            print(sum(balls[:int(query[1])]))
            balls = balls[int(query[1]):]

if __name__ == '__main__':
    main()