def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S1 = S[:i]
        S2 = S[len(S)-len(T)+i:]
        if S1.replace('?','a') == T[:i] and S2.replace('?','a') == T[i:]:
            print('Yes')
        else:
            print('No')
    return
main()

if __name__ == '__main__':
    main()