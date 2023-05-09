def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
    else:
        for i in range(len(S)-1):
            S = S[-1] + S[:-1]
            if S == T:
                print('Yes')
                break
        else:
            print('No')

if __name__ == '__main__':
    main()