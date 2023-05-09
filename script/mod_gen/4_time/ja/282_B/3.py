def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if len(set(S[i]+S[j])) == 1:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()