def main():
    N = int(input())
    S = input()
    ans = ""
    for i in range(len(S)):
        num = ord(S[i]) + N
        if num > 90:
            num -= 26
        ans += chr(num)
    print(ans)

if __name__ == '__main__':
    main()