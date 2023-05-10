def main():
    N = int(input())
    queries = []
    for i in range(N):
        queries.append(input().split())
    #print(queries)
    balls = []
    for i in range(N):
        if queries[i][0] == '1':
            balls.append(int(queries[i][1]))
        elif queries[i][0] == '2':
            for j in range(len(balls)):
                balls[j] += int(queries[i][1])
        elif queries[i][0] == '3':
            print(min(balls))
            balls.remove(min(balls))
    #print(balls)

if __name__ == '__main__':
    main()