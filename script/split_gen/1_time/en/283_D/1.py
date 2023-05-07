def main():
    s = input()
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append("(")
        elif s[i] == ")":
            if len(stack) == 0:
                print("No")
                return
            stack.pop()
        else:
            if s[i] in stack:
                print("No")
                return
            stack.append(s[i])
    print("Yes")
