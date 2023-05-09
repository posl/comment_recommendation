def main():
    S = input()
    stack = []
    for c in S:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if len(stack) == 0 or stack[-1] == ")":
                stack.append(c)
            else:
                stack.pop()
        else:
            if len(stack) == 0:
                stack.append(c)
            elif stack[-1] == ")":
                stack.append(c)
            else:
                stack.pop()
    if len(stack) == 0:
        print("Yes")
    else:
        print("No")
