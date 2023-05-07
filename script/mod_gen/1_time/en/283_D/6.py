def solve():
    S = input()
    stack = []
    for s in S:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if len(stack) == 0 or stack[-1] == ")":
                stack.append(s)
            else:
                stack.pop()
        else:
            if len(stack) == 0 or stack[-1] == ")":
                stack.append(s)
            else:
                stack.pop()
    if len(stack) == 0:
        print("Yes")
    else:
        print("No")
solve()

if __name__ == '__main__':
    solve()