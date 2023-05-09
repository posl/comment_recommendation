def main():
    s = input()
    #stack = []
    stack = 0
    for i in s:
        if i == "(":
            stack += 1
        elif i == ")":
            stack -= 1
        else:
            stack += 1
        if stack < 0:
            print("No")
            return
    if stack == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()