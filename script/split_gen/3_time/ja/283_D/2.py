def main():
    S = input()
    stack = []
    for s in S:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if len(stack) == 0:
                print('No')
                return
            stack.pop()
        else:
            stack.append(s)
    if len(stack) == 0:
        print('Yes')
    else:
        print('No')
