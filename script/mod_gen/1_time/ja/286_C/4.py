def main():
    N, A, B = map(int, input().split())
    S = input()
    S = S + S
    ans = 0
    for i in range(N):
        if S[i] == S[i + N - 1]:
            continue
        else:
            ans += B
    print(ans)

if __name__ == '__main__':
    main()