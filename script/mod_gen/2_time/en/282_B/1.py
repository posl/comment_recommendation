def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if all(S[i][k] == 'o' or S[j][k] == 'o' for k in range(M)):
                count += 1
    print(count)
main()

if __name__ == '__main__':
    main()