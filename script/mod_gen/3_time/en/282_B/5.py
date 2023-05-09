def main():
    N, M = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if [S[i][k] == 'o' or S[j][k] == 'o' for k in range(M)] == [True] * M:
                count += 1
    print(count)

if __name__ == '__main__':
    main()