def main():
    S = input()
    stack = []
    for i in range(len(S)):
        if S[i] == "(":
            stack.append("(")
        elif S[i] == ")":
            if len(stack) == 0:
                print("No")
                return
            else:
                stack.pop()
        else:
            if len(stack) == 0:
                stack.append(S[i])
            elif stack[-1] == "(":
                stack.append(S[i])
            else:
                if stack[-1] == S[i]:
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