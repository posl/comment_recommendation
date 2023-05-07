def main():
    S = input()
    N = len(S)
    ans = N
    for i in range(1, N):
        if S[i] != '0':
            ans = min(ans, i + (N - i + 2) // 3)
    print(ans)

if __name__ == '__main__':
    main()