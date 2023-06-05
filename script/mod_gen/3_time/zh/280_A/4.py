def main():
    h = 0
    w = 0
    while True:
        try:
            h, w = map(int, input().split())
            break
        except:
            print("输入错误")
    count = 0
    for i in range(h):
        s = input()
        for j in range(len(s)):
            if s[j] == "#":
                count += 1
    print(count)

if __name__ == '__main__':
    main()