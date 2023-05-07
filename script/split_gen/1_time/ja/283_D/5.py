def main():
    S = input()
    box = []
    for s in S:
        if s == "(":
            box.append("(")
        elif s == ")":
            if len(box) == 0:
                print("No")
                return
            box.pop()
        else:
            if s in box:
                print("No")
                return
            else:
                box.append(s)
    if len(box) == 0:
        print("Yes")
    else:
        print("No")
