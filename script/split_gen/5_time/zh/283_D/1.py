def main():
    s = input().strip()
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if len(stack) == 0:
                print("否")
                return
            else:
                stack.pop()
        else:
            stack.append(c)
    if len(stack) == 0:
        print("是")
    else:
        print("否")
