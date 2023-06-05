def isGoodString(s):
    if len(s) % 2 == 1:
        return False
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    isGoodString()