def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    cnt = [0] * 26
    for i in range(N):
        for j in range(len(S[i])):
            cnt[ord(S[i][j]) - ord('a')] += 1
    cnt.sort(reverse=True)
    print(sum(cnt[:K]))

if __name__ == '__main__':
    main()