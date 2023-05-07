def main():
    s = input()
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                print('No')
                return
            else:
                stack.pop()
        else:
            continue
    if len(stack) == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()