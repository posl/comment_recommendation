def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(10):
        for j in range(N):
            if S[j][i] == '8':
                ans = max(ans, i + (10 - (j + 1) % 10) % 10)
                break
    print(ans)

if __name__ == '__main__':
    main()