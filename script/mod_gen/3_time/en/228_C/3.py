def main():
    N, K = map(int, input().split())
    score = [list(map(int, input().split())) for _ in range(N)]
    score.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)
    for i in range(N):
        if score[i][0] + score[i][1] + score[i][2] + score[K - 1][3] < score[K - 1][0] + score[K - 1][1] + score[K - 1][2] + score[K - 1][3]:
            print("No")
        else:
            print("Yes")

if __name__ == '__main__':
    main()