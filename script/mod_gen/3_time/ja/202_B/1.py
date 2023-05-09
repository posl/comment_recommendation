def main():
    s = input()
    ans = ''
    for i in s:
        if i == '6':
            ans += '9'
        elif i == '9':
            ans += '6'
        else:
            ans += i
    print(ans[::-1])

if __name__ == '__main__':
    main()