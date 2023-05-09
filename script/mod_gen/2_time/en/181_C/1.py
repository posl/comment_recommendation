def main():
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if (P[i][1] - P[j][1]) * (P[j][0] - P[k][0]) == (P[j][1] - P[k][1]) * (P[i][0] - P[j][0]):
                    print("Yes")
                    return
    print("No")

if __name__ == '__main__':
    main()