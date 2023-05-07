def main():
    S = input()
    print(26**(len(S)-1)*(ord(S[0])-64)+sum([26**(len(S)-i-1)*(ord(S[i])-64) for i in range(1,len(S))]))

if __name__ == '__main__':
    main()