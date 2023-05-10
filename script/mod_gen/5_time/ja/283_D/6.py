def main():
    S = input()
    if len(S) % 2 == 1:
        print('No')
        exit()
    for i in range(len(S)):
        if S[i] == '(':
            continue
        if S[i] == ')':
            if S[:i].count('(') == S[:i].count(')'):
                print('No')
                exit()
    print('Yes')

if __name__ == '__main__':
    main()