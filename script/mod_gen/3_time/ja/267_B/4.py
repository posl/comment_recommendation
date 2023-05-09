def main():
    S = input()
    if S[0] == '0':
        print('No')
        return
    if S[9] == '0':
        print('No')
        return
    if S[1:9].count('1') == 0:
        print('No')
        return
    print('Yes')

if __name__ == '__main__':
    main()