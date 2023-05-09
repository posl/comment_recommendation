def main():
    n = int(input())
    s = input()
    ans = ""
    for i in s:
        ans += chr((ord(i) - ord("A") + n) % 26 + ord("A"))
    print(ans)

if __name__ == '__main__':
    main()