def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(N//2):
        if S[i] == S[N-i-1]:
            continue
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()