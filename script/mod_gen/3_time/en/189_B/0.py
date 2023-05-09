def main():
    N, X = map(int, input().split())
    for i in range(N):
        V, P = map(int, input().split())
        X -= V * P / 100
        if X < 0:
            print(i + 1)
            exit()
    print(-1)

if __name__ == '__main__':
    main()