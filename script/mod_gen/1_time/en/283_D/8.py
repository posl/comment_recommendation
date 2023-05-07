def main():
    S = input()
    a = []
    for i in range(len(S)):
        if S[i] == '(':
            a.append('(')
        elif S[i] == ')':
            if len(a) == 0:
                print('No')
                return
            a.pop()
        else:
            a.append(S[i])
    if len(a) == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()