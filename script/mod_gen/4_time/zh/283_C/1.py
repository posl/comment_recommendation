def main():
    S = input()
    ans = 0
    i = len(S) - 1
    while i >= 0:
        if S[i] == '0':
            ans += 1
        else:
            break
        i -= 1
    print(ans)

if __name__ == '__main__':
    main()