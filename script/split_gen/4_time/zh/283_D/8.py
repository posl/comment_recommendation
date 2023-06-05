def main():
    s = input()
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                print("否")
                return
            else:
                stack.pop()
    if len(stack) == 0:
        print("是")
    else:
        print("否")
