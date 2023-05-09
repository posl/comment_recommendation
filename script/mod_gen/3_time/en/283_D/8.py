def is_good_string(S):
    stack = []
    for s in S:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
        else:
            if stack and stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
    return len(stack) == 0

if __name__ == '__main__':
    is_good_string()