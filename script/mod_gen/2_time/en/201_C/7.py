def main():
    s = input()
    if s[0] == 'o':
        ans = 9*9*9
    elif s[0] == 'x':
        ans = 9*9*8
    else:
        ans = 9*9*9 + 9*9*8
    for i in range(1,10):
        if s[i] == 'o':
            ans *= 9-i
        elif s[i] == 'x':
            ans *= 8-i
        else:
            ans *= 10-i
    print(ans)

if __name__ == '__main__':
    main()