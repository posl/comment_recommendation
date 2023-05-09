def main():
    N = int(input())
    S = input()
    ans = ""
    for i in range(len(S)):
        if ord(S[i]) + N > ord("Z"):
            ans += chr(ord(S[i]) + N - ord("Z") + ord("A") - 1)
        else:
            ans += chr(ord(S[i]) + N)
    print(ans)

if __name__ == '__main__':
    main()