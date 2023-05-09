def main():
    s = input()
    t = input()
    flag = False
    for i in range(len(s)):
        if s[i:] + s[:i] == t:
            flag = True
            break
    if flag:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()