def main():
    S = input()
    S = list(S)
    S.sort()
    ans = 1
    for i in range(1, len(S)):
        if S[i] != S[i-1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()