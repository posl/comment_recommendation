def main():
    S = list(input())
    stack = []
    for s in S:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if len(stack) > 0:
                stack.pop()
            else:
                print("No")
                exit()
        else:
            if s in stack:
                print("No")
                exit()
            else:
                stack.append(s)
    if len(stack) == 0:
        print("Yes")
    else:
        print("No")
