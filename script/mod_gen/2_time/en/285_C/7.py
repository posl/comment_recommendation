def main():
    S = input()
    print(26*int((len(S)-1)/2)+ord(S[0])-ord('A')+1)
main()

if __name__ == '__main__':
    main()