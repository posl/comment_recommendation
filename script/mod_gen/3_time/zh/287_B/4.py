def main():
    N,M = map(int,input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    count = 0
    for i in range(M):
        for j in range(N):
            if T[i] == S[j][-3:]:
                count += 1
                break
    print(count)

if __name__ == '__main__':
    main()