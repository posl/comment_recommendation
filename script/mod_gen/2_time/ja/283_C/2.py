def main():
    s = input()
    ans = len(s)
    if s[0] == '1':
        ans -= 1
    print(ans)

if __name__ == '__main__':
    main()