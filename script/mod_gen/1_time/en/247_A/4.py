def main():
    s = input()
    ans = ''
    for i in range(3):
        ans += str(int(s[i]))
    ans += '0'
    print(ans)

if __name__ == '__main__':
    main()