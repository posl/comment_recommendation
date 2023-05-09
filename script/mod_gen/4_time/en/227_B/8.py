def main():
    N = int(input())
    S = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(1, N):
            if i + j >= N:
                break
            if 4 * S[i] * S[i + j] + 3 * S[i] + 3 * S[i + j] == 4 * 3 * 3:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()