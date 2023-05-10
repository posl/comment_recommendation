def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
        return
    else:
        for i in range(len(S)-1):
            if S[i] == S[i+1]:
                S = S[:i+1] + S[i] + S[i+1:]
                if S == T:
                    print('Yes')
                    return
        print('No')
        return

if __name__ == '__main__':
    main()