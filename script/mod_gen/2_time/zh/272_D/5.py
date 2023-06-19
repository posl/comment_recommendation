def main():
    N, M = map(int, input().split())
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                print(0, end=' ')
            elif i == 0:
                print(1, end=' ')
            elif j == 0:
                print(1, end=' ')
            else:
                print(2, end=' ')
        print()

if __name__ == '__main__':
    main()