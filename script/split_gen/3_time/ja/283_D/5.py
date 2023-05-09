def main():
    s = input()
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            if len(stack) == 0:
                print('No')
                return
            stack.pop()
        else:
            pass
    if len(stack) == 0:
        print('Yes')
    else:
        print('No')
