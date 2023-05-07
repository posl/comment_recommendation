def main():
    S = input()
    box = []
    for s in S:
        if s == "(":
            box.append(s)
        elif s == ")":
            if len(box) > 0 and box[-1] == "(":
                box.pop()
            else:
                box.append(s)
        else:
            if s in box:
                box.remove(s)
            else:
                box.append(s)
    if box == []:
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()