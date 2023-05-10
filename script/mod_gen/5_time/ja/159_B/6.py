def main():
    S = input()
    if S == S[::-1]:
        if S[:(len(S)-1)//2] == S[:(len(S)-1)//2][::-1]:
            if S[(len(S)+3)//2-1:] == S[(len(S)+3)//2-1:][::-1]:
                print('Yes')
            else:
                print('No')
        else:
            print('No')
    else:
        print('No')

if __name__ == '__main__':
    main()