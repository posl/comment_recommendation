def main():
    N, M = map(int, input().split())
    for i in range(1, M - N + 2):
        for j in range(i + 1, M - N + 3):
            for k in range(j + 1, M - N + 4):
                print(i, j, k)
main()

if __name__ == '__main__':
    main()