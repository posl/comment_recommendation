def main():
    S = input()
    s = []
    for i in range(len(S)):
        if S[i] == '(':
            s.append('(')
        elif S[i] == ')':
            if len(s) == 0:
                print('No')
                return
            else:
                s.pop()
        else:
            s.append(S[i])
    if len(s) == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()