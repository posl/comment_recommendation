def main():
    S = input()
    stack = []
    for s in S:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if stack:
                stack.pop()
            else:
                print("No")
                return
        else:
            if stack:
                stack.pop()
                stack.append(s)
    if stack:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()