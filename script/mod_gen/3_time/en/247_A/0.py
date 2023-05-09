def main():
    s = input()
    ans = ""
    for i in range(4):
        if i == 3:
            ans += "0"
        else:
            ans += s[i]
    print(ans)

if __name__ == '__main__':
    main()