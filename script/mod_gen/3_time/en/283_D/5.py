def main():
    S = input()
    stack = []
    for i in range(len(S)):
        if S[i] == "(":
            stack.append(i)
        elif S[i] == ")":
            if len(stack) == 0:
                print("No")
                return
            else:
                stack.pop()
        else:
            if len(stack) != 0:
                print("No")
                return
    if len(stack) != 0:
        print("No")
    else:
        print("Yes")
    return

if __name__ == '__main__':
    main()