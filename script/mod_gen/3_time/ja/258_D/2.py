def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    time = 0
    for i in range(N):
        time += AB[i][0] * AB[i][1]
    time += AB[0][0] * AB[0][1]
    time += AB[0][0] * AB[0][1]
    for i in range(1, N):
        time += AB[i][0] * AB[i][1]
    print(time)

if __name__ == '__main__':
    main()