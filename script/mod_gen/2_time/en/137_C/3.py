def main():
    N = int(input())
    S = [input() for i in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            if sorted(S[i]) == sorted(S[j]):
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()