def main():
    S = input()
    if S.count('0') > 0:
        print('Yes')
        return
    if len(S) < 2:
        print('No')
        return
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            if int(S[i] + S[j]) % 8 == 0:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()