def main():
    N = int(input())
    S = input()
    ans = ''
    for i in range(len(S)):
        if ord(S[i]) + N > 90:
            ans += chr(ord(S[i]) + N - 26)
        else:
            ans += chr(ord(S[i]) + N)
    print(ans)

if __name__ == '__main__':
    main()