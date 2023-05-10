def main():
    s = input()
    t = input()
    if len(s) < len(t):
        print('No')
        exit()
    for i in range(len(s) - len(t) + 1):
        flag = True
        for j in range(len(t)):
            if s[i + j] != '?' and s[i + j] != t[j]:
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()