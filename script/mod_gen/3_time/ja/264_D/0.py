def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if S[i] != 'a' and S[i] != 't' and S[i] != 'c' and S[i] != 'o' and S[i] != 'd' and S[i] != 'e' and S[i] != 'r':
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()