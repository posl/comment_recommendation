def main():
    N = int(input())
    S = [input() for i in range(N)]
    ans = 0
    for i in range(N):
        ans += 1
        for j in range(10):
            if S[i][j] == str((ans % 10)):
                break
    print(ans)

if __name__ == '__main__':
    main()