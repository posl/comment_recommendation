def is_good_string(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return True if len(stack) == 0 else False
