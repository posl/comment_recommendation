def main():
    s = input()
    stack = []
    for c in s:
        if c == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)
    print('否' if len(stack) > 0 else '是')
