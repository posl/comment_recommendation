def main():
    N, M = map(int, input().split())
    for i in range(N):
        for j in range(N):
            if (i+1) == 1 and (j+1) == 1:
                print(0, end=' ')
            else:
                print(-1, end=' ')
        print()

if __name__ == '__main__':
    main()