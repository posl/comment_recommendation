def main():
    S = input()
    s = list(S)
    n = len(s)
    box = []
    for i in range(n):
        if s[i] == '(':
            box.append(i)
        elif s[i] == ')':
            box.pop()
        else:
            pass
    print(box)

if __name__ == '__main__':
    main()