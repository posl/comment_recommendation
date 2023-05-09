def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    count = 0
    for i in range(N):
        for j in range(M):
            if S[i][-3:] == T[j]:
                count += 1
    print(count)

if __name__ == '__main__':
    main()