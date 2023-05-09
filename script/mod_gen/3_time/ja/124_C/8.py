def main():
    s = input()
    # 0, 1の連続する部分をカウントする
    cnt = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            cnt += 1
    print((cnt+1)//2)

if __name__ == '__main__':
    main()