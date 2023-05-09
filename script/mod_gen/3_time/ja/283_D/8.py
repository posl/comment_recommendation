def main():
    S = input()
    stack = []
    for s in S:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if not stack:
                print('No')
                return
            if stack[-1] == '(':
                stack.pop()
            else:
                print('No')
                return
        else:
            stack.append(s)
    if stack:
        print('No')
    else:
        print('Yes')
main()

if __name__ == '__main__':
    main()