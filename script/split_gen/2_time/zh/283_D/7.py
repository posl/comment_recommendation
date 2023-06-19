def main():
    s = input()
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            if len(stack) == 0:
                print('否')
                exit()
            stack.pop()
    if len(stack) == 0:
        print('是')
    else:
        print('否')
