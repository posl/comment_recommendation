def main():
    s = input()
    if s[0] == "o":
        ans = 1
    elif s[0] == "x":
        ans = 0
    else:
        ans = 10
    for i in range(1, 10):
        if s[i] == "o":
            ans *= 10 - i
        elif s[i] == "x":
            continue
        else:
            ans *= 9 - i
    print(ans)

if __name__ == '__main__':
    main()