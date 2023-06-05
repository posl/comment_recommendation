def main():
    s = input()
    k = int(input())
    if k <= len(s):
        print(s[k-1])
        return
    else:
        num = 0
        for i in s:
            num = num*10 + int(i)
        print(num)
        return

if __name__ == '__main__':
    main()