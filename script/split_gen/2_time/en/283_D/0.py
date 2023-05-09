def main():
    s = input()
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0 or stack[-1] != '(':
                print('No')
                return
            stack.pop()
        else:
            stack.append(c)
    print('Yes' if len(stack) == 0 else 'No')
