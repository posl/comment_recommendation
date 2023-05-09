def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    for i in range(N):
        if X >= AB[i][0] * AB[i][1]:
            X -= AB[i][0] * AB[i][1]
        else:
            X %= AB[i][0]
    if X == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()