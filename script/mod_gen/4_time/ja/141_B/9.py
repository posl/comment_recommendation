def main():
    s = str(input())
    s = list(s)
    flag = True
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == "L":
                flag = False
        else:
            if s[i] == "R":
                flag = False
    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()