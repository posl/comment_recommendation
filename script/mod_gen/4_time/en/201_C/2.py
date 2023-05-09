def main():
    s = input()
    if s[0] == 'x':
        print(0)
        return
    ans = 1
    for i in range(1, 10):
        if s[i] == 'o':
            ans *= 9 - i
        elif s[i] == 'x':
            ans *= i
    print(ans)

if __name__ == '__main__':
    main()