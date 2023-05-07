def main():
    s = input()
    s = s.replace('a', '').replace('b', '').replace('c', '')
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                print('No')
                return
            stack.pop()
    if len(stack) == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()