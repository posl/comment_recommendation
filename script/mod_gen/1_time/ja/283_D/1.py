def main():
    S = input()
    stack = []
    for i in range(len(S)):
        if S[i] == "(":
            stack.append(S[i])
        elif S[i] == ")":
            if len(stack) == 0:
                print("No")
                exit()
            else:
                stack.pop()
        else:
            continue
    if len(stack) == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()