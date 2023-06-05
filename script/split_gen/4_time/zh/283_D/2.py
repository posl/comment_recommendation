def main():
    s = input()
    n = len(s)
    stack = []
    for i in range(n):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')' and stack[-1] == i - 1:
            stack.pop()
        elif s[i] == ')' and stack[-1] != i - 1:
            stack.append(i)
        else:
            pass
    if len(stack) == 0:
        print('是')
    else:
        print('否')
main()
