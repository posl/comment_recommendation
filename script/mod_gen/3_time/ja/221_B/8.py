def main():
    s = input()
    t = input()
    ans = 'Yes'
    for i in range(len(s)):
        if s[i] != t[i]:
            if s[i+1:] == t[i+1:]:
                print(ans)
                return
            else:
                ans = 'No'
    print(ans)

if __name__ == '__main__':
    main()