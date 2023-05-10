def main():
    s = input()
    stack = []
    for i in range(len(s)):
        c = s[i]
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                print("No")
                return
            else:
                stack.pop()
    if len(stack) == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()