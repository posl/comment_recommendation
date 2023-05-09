def main():
    S = input()
    stack = []
    for s in S:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if len(stack) == 0:
                print("No")
                return
            stack.pop()
        else:
            if s in stack:
                print("No")
                return
            stack.append(s)
    if len(stack) == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()