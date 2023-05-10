def main():
    s = input()
    k = int(input())
    if k < len(s):
        print(s[k-1])
        return
    else:
        if s[0] == '1':
            for i in range(len(s)):
                if s[i] != '1':
                    print(s[i])
                    return
        else:
            print(s[0])
            return

if __name__ == '__main__':
    main()