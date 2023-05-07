def main():
    s = input()
    n = len(s)
    if n == 1:
        print(0)
        return
    if n == 2:
        if s[0] == s[1]:
            print(1)
        else:
            print(0)
        return
    # 連続する0の数
    zero = 0
    # 連続する1の数
    one = 0
    for i in range(n):
        if s[i] == "0":
            zero += 1
        else:
            one += 1
    print(min(zero, one))
main()

if __name__ == '__main__':
    main()