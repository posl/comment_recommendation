def main():
    s = input()
    ans = ""
    for i in range(len(s)-1):
        ans += str(int(s[i] == "1"))
    ans += "0"
    print(ans)

if __name__ == '__main__':
    main()