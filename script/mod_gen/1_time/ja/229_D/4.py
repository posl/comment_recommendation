def main():
    S = input()
    K = int(input())
    N = len(S)
    ans = 0
    for i in range(N):
        for j in range(i, N):
            ans = max(ans, j - i + 1 - S[i:j+1].count("X"))
    print(min(ans + K, N))

if __name__ == '__main__':
    main()