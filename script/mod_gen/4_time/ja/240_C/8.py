def main():
    N, X = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(N)]
    sum = 0
    for i in range(N):
        sum += ab[i][0] * ab[i][1]
        if sum > X * 100:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()