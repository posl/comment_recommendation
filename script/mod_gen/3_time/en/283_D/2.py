def main():
    s = input()
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if len(stack) == 0:
                print("No")
                return
            stack.pop()
        else:
            if c in stack:
                print("No")
                return
            stack.append(c)
    if len(stack) == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()