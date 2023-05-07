def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            flag = True
            for k in range(M):
                if S[i][k] != S[j][k]:
                    flag = False
                    break
            if flag:
                count += 1
    print(count)

if __name__ == '__main__':
    main()