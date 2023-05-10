def main():
    N = int(input())
    S = input()
    ans = ""
    for i in range(len(S)):
        ans += chr(((ord(S[i]) - ord('A') + N) % 26) + ord('A'))
    print(ans)

if __name__ == '__main__':
    main()