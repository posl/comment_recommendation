def main():
    # input
    S = input()
    # compute
    ans = 0
    for i in range(len(S)):
        ans += (ord(S[i])-ord('A')+1) * 26**(len(S)-i-1)
    # output
    print(ans)

if __name__ == '__main__':
    main()