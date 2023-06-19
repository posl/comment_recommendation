def main():
    S = input()
    stack = []
    for c in S:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if len(stack) == 0:
                print("No")
                return
            else:
                stack.pop()
        else:
            if len(stack) == 0:
                print("No")
                return
    if len(stack) == 0:
        print("Yes")
    else:
        print("No")
main()
