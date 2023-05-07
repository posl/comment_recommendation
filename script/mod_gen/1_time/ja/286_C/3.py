def main():
    N, A, B = map(int, input().split())
    S = input()
    ans = 0
    if S == S[::-1]:
        print(ans)
        return
    for i in range(N//2):
        if S[i] != S[N-1-i]:
            ans += min(A, B)
    print(ans)

if __name__ == '__main__':
    main()