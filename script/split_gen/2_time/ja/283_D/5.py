def main():
    S = input()
    #S = "(((())))"
    #S = "((a)ba)"
    #S = "(a(ba))"
    #S = "abca"
    box = []
    for i in S:
        if i == "(":
            box.append(i)
        elif i == ")":
            if len(box) == 0:
                print("No")
                return
            box.pop()
        else:
            box.append(i)
    if len(box) == 0:
        print("Yes")
    else:
        print("No")
