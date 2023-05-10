def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        ans += (ord(S[i])-64) * (26**(len(S)-i-1))
    print(ans)

if __name__ == '__main__':
    main()