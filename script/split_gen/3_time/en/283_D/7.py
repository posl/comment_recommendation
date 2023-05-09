def main():
    S = input()
    box = []
    for c in S:
        if c == '(':
            box.append(c)
        elif c == ')':
            if len(box) > 0 and box[-1] == '(':
                box.pop()
            else:
                box.append(c)
        else:
            if c in box:
                box.append(c)
            else:
                box = [c]
    if len(box) == 0:
        print("Yes")
    else:
        print("No")
main()
