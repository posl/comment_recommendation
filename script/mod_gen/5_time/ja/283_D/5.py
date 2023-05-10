def main():
    s = input()
    n = len(s)
    stack = []
    for i in range(n):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            if len(stack) == 0:
                print('No')
                return
            stack.pop()
    if len(stack) > 0:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()