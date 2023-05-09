def main():
    S = input()
    if S[0] == "o":
        ans = 9 * 9 * 9 * 8
    elif S[0] == "x":
        ans = 9 * 9 * 9 * 9
    else:
        ans = 9 * 9 * 9 * 9 + 9 * 9 * 9 * 8
    for i in range(1, 10):
        if S[i] == "o":
            ans *= 9 - i
        elif S[i] == "x":
            ans *= 10 - 1 - i
        else:
            ans *= 10 - i
    print(ans)

if __name__ == '__main__':
    main()