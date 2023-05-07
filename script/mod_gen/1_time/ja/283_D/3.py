def main():
    S = input()
    stack = []
    for i in S:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                print("No")
                return
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()