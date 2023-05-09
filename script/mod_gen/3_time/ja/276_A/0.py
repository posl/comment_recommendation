def main():
    s = input()
    ans = -1
    for i in range(len(s)):
        if s[i] == 'a':
            ans = i + 1
    print(ans)

if __name__ == '__main__':
    main()