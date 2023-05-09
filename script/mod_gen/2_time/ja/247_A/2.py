def main():
    s = input()
    ans = ''
    for i in range(3):
        if s[i] == '1':
            ans += '1'
        else:
            ans += '0'
    if s[3] == '1':
        ans += '0'
    else:
        ans += '0'
    print(ans)

if __name__ == '__main__':
    main()