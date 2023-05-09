def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(10):
        c = 0
        for j in range(N):
            c = max(c, S[j].count(str(i)))
        ans += c
    print(ans)

if __name__ == '__main__':
    main()