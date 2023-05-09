def main():
    S = input()
    stack = []
    for s in S:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if len(stack) == 0 or stack.pop() != '(':
                print('No')
                return
        else:
            if len(stack) > 0:
                stack.pop()
    if len(stack) == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()