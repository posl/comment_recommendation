def main():
    S = input()
    stack = []
    for i in range(len(S)):
        if S[i] == ')':
            if len(stack) == 0:
                print("No")
                return
            else:
                stack.pop()
        elif S[i] == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                print("No")
                return
    if len(stack) == 0:
        print("Yes")
    else:
        print("No")
    return

if __name__ == '__main__':
    main()