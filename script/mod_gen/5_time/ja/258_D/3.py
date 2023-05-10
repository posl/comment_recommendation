def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1], reverse=True)
    time = 0
    for i in range(N):
        time += AB[i][0] * AB[i][1]
        if time > X:
            print(time + AB[i][0] * (X - time) // AB[i][1])
            return
    print(time)

if __name__ == '__main__':
    main()