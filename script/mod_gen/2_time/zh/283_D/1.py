def main():
    line = input()
    if line == '':
        return
    stack = []
    for i in range(len(line)):
        if line[i] == '(':
            stack.append(i)
        elif line[i] == ')':
            if len(stack) == 0:
                print('否')
                return
            else:
                stack.pop()
    if len(stack) == 0:
        print('是')
    else:
        print('否')

if __name__ == '__main__':
    main()