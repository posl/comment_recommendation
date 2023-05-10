def check(s):
    if len(s) == 0:
        return True
    if len(s) == 1:
        return False
    if s[0] == ")":
        return False
    if s[-1] == "(":
        return False
    if s[0] == "(" and s[-1] == ")":
        return check(s[1:-1])
    return False
s = input()
ans = True
stack = []
for i in range(len(s)):
    if s[i] == "(":
        stack.append("(")
    elif s[i] == ")":
        if len(stack) == 0:
            ans = False
            break
        else:
            stack.pop()
    else:
        if len(stack) == 0:
            ans = False
            break
        else:
            stack.pop()
