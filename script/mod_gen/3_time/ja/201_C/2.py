def main():
    s = input()
    if s[0] == "o":
        ans = 1
    elif s[0] == "x":
        ans = 0
    else:
        ans = 3
    for i in range(1, 10):
        if s[i] == "o":
            if i == 0:
                ans *= 9
            else:
                ans *= 10
        elif s[i] == "x":
            if i == 0:
                ans *= 0
            else:
                ans *= 9
        else:
            if i == 0:
                ans *= 9
            else:
                ans *= 10
    print(ans)

if __name__ == '__main__':
    main()