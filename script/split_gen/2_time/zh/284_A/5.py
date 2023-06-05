def main():
    S = input()
    stack = []
    for c in S:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                print('否')
                return
    if stack:
        print('否')
    else:
        print('是')
