def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S_ = S[:i] + S[len(S)-len(T)+i:]
        for j in range(len(T)):
            if S_[j] == '?' or S_[j] == T[j]:
                continue
            else:
                print('No')
                break
        else:
            print('Yes')

if __name__ == '__main__':
    main()