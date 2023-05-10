def main():
    S = input()
    ans = 0
    for i in range(4):
        if S[i] == '+':
            ans += 1
        else:
            ans -= 1
    print(ans)
    return 0

if __name__ == '__main__':
    main()