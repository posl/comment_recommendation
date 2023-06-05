def main():
    q = int(input())
    balls = []
    for i in range(q):
        query = input()
        if query[0] == '1':
            x, c = query.split()[1:]
            balls.extend([int(x)] * int(c))
        else:
            c = int(query.split()[1])
            print(sum(balls[:c]))
            balls = balls[c:]

if __name__ == '__main__':
    main()