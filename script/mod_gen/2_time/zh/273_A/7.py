def main():
    N, M = map(int, input().split())
    for i in range(N):
        for j in range(N):
            if i == j:
                print(0, end=' ')
            elif i < j:
                print(i + j, end=' ')
            else:
                print(j + i, end=' ')
        print()

if __name__ == '__main__':
    main()