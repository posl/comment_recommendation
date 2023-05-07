def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(N):
        if i == 0:
            ans += int(S[i])
        else:
            if int(S[i]) == 0:
                ans += 1
            else:
                ans += int(S[i]) + 1
    print(ans)

if __name__ == '__main__':
    main()