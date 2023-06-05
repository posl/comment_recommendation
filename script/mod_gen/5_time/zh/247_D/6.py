def main():
    q = int(input())
    queries = [input().split() for _ in range(q)]
    balls = []
    for query in queries:
        if query[0] == '1':
            balls.extend([query[1]] * int(query[2]))
        else:
            print(sum(map(int, balls[:int(query[1])])))
            balls = balls[int(query[1]):]

if __name__ == '__main__':
    main()