def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
        return
    for i in range(len(S)-1):
        tmp = list(S)
        tmp[i], tmp[i+1] = tmp[i+1], tmp[i]
        if ''.join(tmp) == T:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()