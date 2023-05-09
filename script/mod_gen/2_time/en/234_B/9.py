def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    max = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            else:
                length = ((A[i][0] - A[j][0]) ** 2 + (A[i][1] - A[j][1]) ** 2) ** 0.5
                if length > max:
                    max = length
    print(max)

if __name__ == '__main__':
    main()