def main():
    s = input()
    stack = []
    for c in s:
        if c == ")":
            if len(stack) == 0:
                print("No")
                return
            if stack[-1] == "(":
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)
    if len(stack) == 0:
        print("Yes")
    else:
        print("No")
