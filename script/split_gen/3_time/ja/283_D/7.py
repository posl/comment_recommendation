def main():
    s = input()
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        elif s[i] == ")":
            if stack:
                stack.pop()
            else:
                print("No")
                return
        else:
            if stack:
                stack.pop()
    if stack:
        print("No")
    else:
        print("Yes")
