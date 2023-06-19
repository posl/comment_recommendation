def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print('No')
        return
    alphabets = [0] * 26
    for i in range(len(S)):
        alphabets[ord(S[i]) - ord('a')] += 1
        alphabets[ord(T[i]) - ord('a')] -= 1
    for i in range(26):
        if alphabets[i] != 0:
            print('No')
            return
    print('Yes')
    return

if __name__ == '__main__':
    main()