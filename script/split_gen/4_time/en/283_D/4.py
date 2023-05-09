def main():
    s = input()
    n = len(s)
    if n % 2 != 0:
        print('No')
        return
    stack = []
    for i in range(n):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            if len(stack) == 0:
                print('No')
                return
            stack.pop()
    if len(stack) != 0:
        print('No')
        return
    print('Yes')
