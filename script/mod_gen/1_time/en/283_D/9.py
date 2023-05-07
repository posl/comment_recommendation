def main():
    S = input()
    S = S.replace('a','').replace('b','').replace('c','')
    if S == '':
        print('Yes')
        return
    if len(S)%2 == 1:
        print('No')
        return
    if S[0] != '(' or S[-1] != ')':
        print('No')
        return
    stack = []
    for s in S:
        if s == '(':
            stack.append(s)
        else:
            if stack[-1] == '(':
                stack.pop()
            else:
                print('No')
                return
    if len(stack) == 0:
        print('Yes')
    else:
        print('No')
    return

if __name__ == '__main__':
    main()