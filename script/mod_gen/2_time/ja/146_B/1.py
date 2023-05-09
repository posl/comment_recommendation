def main():
    n = int(input())
    s = input()
    ans = ""
    for i in s:
        if ord(i) + n > ord("Z"):
            ans += chr(ord(i) + n - ord("Z") + ord("A") - 1)
        else:
            ans += chr(ord(i) + n)
    print(ans)

if __name__ == '__main__':
    main()