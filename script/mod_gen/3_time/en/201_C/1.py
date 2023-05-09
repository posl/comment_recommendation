def main():
    S = input()
    if S[0] == 'x':
        print(0)
        return
    if S[0] == '?':
        ans = 9
    else:
        ans = 1
    for i in range(1, 10):
        if S[i] == 'o':
            if S[i-1] == 'o':
                ans *= 9
            elif S[i-1] == '?':
                ans *= 10
        elif S[i] == 'x':
            if S[i-1] == 'o':
                ans *= 0
            elif S[i-1] == '?':
                ans *= 1
        elif S[i] == '?':
            if S[i-1] == 'o':
                ans *= 9
            elif S[i-1] == '?':
                ans *= 10
        ans %= 1000000007
    print(ans)

if __name__ == '__main__':
    main()