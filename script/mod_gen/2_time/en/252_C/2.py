def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(10):
        cnt = 0
        for j in range(N):
            cnt = max(cnt, S[j].index(str(i)))
        ans += cnt
    print(ans)

if __name__ == '__main__':
    main()